"""Cards for the RWA Oracle Scorecard ranking page, in the blog's own
(not the scorecard app's) visual style -- plain dicts in, no State."""

import reflex as rx

from ..data.rwa_scorecard import format_iso_utc
from ..theme import BORDER, Color, RADIUS_MD, RADIUS_SM

SCORE_GOOD = "#1F9D55"
SCORE_OK = "#B7791F"
SCORE_BAD = "#C0392B"

SCORE_GOOD_THRESHOLD = 85
SCORE_OK_THRESHOLD = 60

QUESTION_ORDER = ["freshness", "supply", "price", "concentration"]
QUESTION_SHORT_LABELS = {
    "freshness": "Freshness",
    "supply": "Supply",
    "price": "Price",
    "concentration": "Control",
}


def score_color(score: int | None) -> str:
    if score is None:
        return Color.text_faint
    if score >= SCORE_GOOD_THRESHOLD:
        return SCORE_GOOD
    if score >= SCORE_OK_THRESHOLD:
        return SCORE_OK
    return SCORE_BAD


def score_badge(score: int | None) -> rx.Component:
    return rx.box(
        rx.text(
            score if score is not None else "—",
            size="4",
            weight="bold",
            color=Color.bg,
        ),
        background=score_color(score),
        border_radius="999px",
        width="2.75rem",
        height="2.75rem",
        display="flex",
        align_items="center",
        justify_content="center",
        flex_shrink="0",
    )


def _category_pill(category: str) -> rx.Component:
    return rx.box(
        rx.text(category, size="1", weight="medium", color=Color.accent),
        padding_x="0.6rem",
        padding_y="0.2rem",
        border_radius="999px",
        background=Color.accent_soft,
    )


_STATUS_LABELS = {
    "not_applicable": "N/A",
    "not_published": "Not published (0)",
    "unresolved": "Not verified",
    "error": "Error",
}


def _question_value_display(question: dict) -> str:
    """Never a bare '—': a missing score always says *why* it's missing,
    using the status the pipeline actually reported -- see
    _question_bar's docstring-equivalent note on why this must read the
    question's own status rather than guess from the score alone."""
    score = question["score"]
    if score is not None:
        return str(score)
    return _STATUS_LABELS.get(question["status"], "N/A")


def _question_bar(question: dict) -> rx.Component:
    label = QUESTION_SHORT_LABELS[question["name"]]
    score = question["score"]
    return rx.box(
        rx.flex(
            rx.text(label, size="1", color=Color.text_muted, width="4.5rem", flex_shrink="0"),
            rx.box(
                rx.box(
                    width=f"{score}%" if score is not None else "0%",
                    height="100%",
                    background=score_color(score),
                    border_radius=RADIUS_SM,
                ),
                width="100%",
                height="0.4rem",
                background=Color.border,
                border_radius=RADIUS_SM,
                overflow="hidden",
                flex="1",
            ),
            rx.text(
                _question_value_display(question),
                size="1",
                color=Color.text_faint,
                width="6rem",
                text_align="right",
                flex_shrink="0",
                white_space="nowrap",
            ),
            align="center",
            gap="0.5rem",
        ),
        margin_bottom="0.4rem",
    )


def _keys_to_lie_display(entry: dict) -> str:
    """Reads the concentration question's own status rather than just
    checking whether min_keys_to_lie is None -- None covers two distinct,
    very different cases (not_published: no classifiable control role at
    all; unresolved: a role holder exists but we couldn't classify it),
    and showing "unresolved" for a not_published asset misrepresents one
    as the other."""
    keys = entry["min_keys_to_lie"]
    if keys is not None:
        plural = "s" if keys != 1 else ""
        return f"{keys} key{plural} to lie"
    concentration = next(q for q in entry["questions"] if q["name"] == "concentration")
    return f"Control: {_STATUS_LABELS.get(concentration['status'], 'N/A')}"


def asset_card(entry: dict, rank: int | None = None) -> rx.Component:
    """Card for a ranked (or close to ranked) asset: rank, symbol, overall
    score, the 4 question mini-bars, coverage and keys-to-lie."""
    questions_by_name = {q["name"]: q for q in entry["questions"]}
    return rx.box(
        rx.hstack(
            rx.text(
                f"#{rank}", size="2", weight="bold", color=Color.text_faint, flex_shrink="0"
            )
            if rank is not None
            else rx.box(),
            score_badge(entry["overall_score"]),
            rx.vstack(
                rx.text(entry["symbol"], size="4", weight="bold", color=Color.text),
                rx.text(entry["name"], size="2", color=Color.text_muted),
                spacing="0",
                align="start",
            ),
            spacing="3",
            align="center",
        ),
        rx.box(
            *[_question_bar(questions_by_name[name]) for name in QUESTION_ORDER],
            margin_top="1.1rem",
        ),
        rx.flex(
            _category_pill(entry["category"]),
            rx.text(
                f"{entry['coverage_pct']}% coverage",
                size="1",
                color=Color.text_faint,
            ),
            justify="between",
            align="center",
            width="100%",
            margin_top="0.85rem",
        ),
        rx.text(
            _keys_to_lie_display(entry),
            size="1",
            color=Color.text_faint,
            margin_top="0.35rem",
        ),
        rx.link(
            "Details →",
            href=f"/projects/rwa-scorecard/{entry['slug']}",
            size="1",
            color=Color.accent,
            margin_top="0.75rem",
            display="inline-block",
        ),
        width="100%",
        border=BORDER,
        border_radius=RADIUS_MD,
        padding="1.25rem",
        background=Color.bg,
    )


def provisional_asset_card(entry: dict) -> rx.Component:
    """Same shell as asset_card, but greyed out with the reason it isn't
    ranked yet -- never mixed visually with a normal, lower-scoring entry."""
    return rx.box(
        rx.hstack(
            score_badge(entry["overall_score"]),
            rx.vstack(
                rx.text(entry["symbol"], size="4", weight="bold", color=Color.text),
                rx.text(entry["name"], size="2", color=Color.text_muted),
                spacing="0",
                align="start",
            ),
            spacing="3",
            align="center",
        ),
        rx.text(
            entry["provisional_reason"] or "Not yet ranked.",
            size="1",
            color=Color.text_muted,
            margin_top="0.85rem",
        ),
        rx.flex(
            _category_pill(entry["category"]),
            rx.text(
                f"{entry['coverage_pct']}% coverage",
                size="1",
                color=Color.text_faint,
            ),
            justify="between",
            align="center",
            width="100%",
            margin_top="0.85rem",
        ),
        rx.link(
            "Details →",
            href=f"/projects/rwa-scorecard/{entry['slug']}",
            size="1",
            color=Color.accent,
            margin_top="0.75rem",
            display="inline-block",
        ),
        width="100%",
        border=BORDER,
        border_radius=RADIUS_MD,
        padding="1.25rem",
        background=Color.bg,
        opacity="0.6",
    )


_STATUS_LABELS_LONG = {
    "measured": "Measured",
    "self_reported": "Self-reported (capped)",
    "disputed": "Disputed",
    "not_applicable": "Not applicable",
    "not_published": "Not published",
    "unresolved": "Not verified",
    "error": "Error",
}


def control_summary_display(entry: dict) -> str:
    """"N keys can change this token" for the token detail page -- unlike
    _keys_to_lie_display (the ranking card's "N keys to lie" framing),
    used where the question being answered is "who can change this
    token's rules", not "how easy would it be to lie about its data"."""
    keys = entry["min_keys_to_lie"]
    if keys is not None:
        plural = "s" if keys != 1 else ""
        return f"{keys} key{plural} can change this token"
    concentration = next(q for q in entry["questions"] if q["name"] == "concentration")
    return _STATUS_LABELS_LONG.get(concentration["status"], "Not applicable")


def question_detail_card(question: dict) -> rx.Component:
    """One card per question on a token's detail page: status, score,
    reason, and as-of date/source when the pipeline has them."""
    score = question["score"]
    return rx.box(
        rx.flex(
            rx.heading(question["label"], size="4", color=Color.text),
            rx.box(
                rx.text(
                    str(score) if score is not None else "—",
                    size="4",
                    weight="bold",
                    color=Color.bg,
                ),
                background=score_color(score),
                border_radius="999px",
                width="2.5rem",
                height="2.5rem",
                display="flex",
                align_items="center",
                justify_content="center",
                flex_shrink="0",
            ),
            justify="between",
            align="center",
            width="100%",
        ),
        rx.text(
            _STATUS_LABELS_LONG.get(question["status"], question["status"]),
            size="1",
            weight="medium",
            color=Color.accent,
            text_transform="uppercase",
            letter_spacing="0.05em",
            margin_top="0.5rem",
        ),
        rx.text(question["reason"], size="2", color=Color.text_muted, margin_top="0.75rem"),
        rx.flex(
            rx.text(
                f"As of {format_iso_utc(question['as_of'])}" if question["as_of"] else "As of: unknown",
                size="1",
                color=Color.text_faint,
            ),
            rx.text(
                question["source"] or "Source: unspecified",
                size="1",
                color=Color.text_faint,
            ),
            direction="column",
            gap="0.2rem",
            margin_top="0.85rem",
        ),
        width="100%",
        border=BORDER,
        border_radius=RADIUS_MD,
        padding="1.5rem",
        background=Color.bg,
    )
