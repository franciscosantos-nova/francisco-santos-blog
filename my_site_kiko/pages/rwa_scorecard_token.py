"""One static page per tracked token, e.g. /projects/rwa-scorecard/usdc --
same closure-based pattern as post_detail.py's per-post pages, built at
compile time from data/rwa_scorecard.py, no State, no live backend.
"""

import reflex as rx

from ..components.layout import page_shell
from ..components.scorecard_cards import (
    QUESTION_ORDER,
    control_summary_display,
    score_badge,
)
from ..components.scorecard_cards import question_detail_card
from ..theme import BORDER, Color, Spacing


def _token_header(entry: dict) -> rx.Component:
    return rx.box(
        rx.box(
            entry["category"],
            padding_x="0.6rem",
            padding_y="0.2rem",
            border_radius="999px",
            background=Color.accent_soft,
            color=Color.accent,
            font_size="0.75rem",
            font_weight="medium",
            display="inline-block",
        ),
        rx.heading(entry["symbol"], as_="h1", size="8", weight="bold", margin_top="0.5rem"),
        rx.text(entry["name"], size="3", color=Color.text_muted),
        rx.text(
            f"Issued by {entry['issuer']}",
            size="2",
            color=Color.text_faint,
            margin_top="0.25rem",
        ),
        margin_bottom="1.5rem",
    )


def _overall_summary(entry: dict) -> rx.Component:
    return rx.box(
        rx.hstack(
            score_badge(entry["overall_score"]),
            rx.vstack(
                rx.text(
                    "Overall trust score",
                    size="1",
                    text_transform="uppercase",
                    letter_spacing="0.06em",
                    color=Color.text_faint,
                ),
                rx.text(f"{entry['coverage_pct']}% coverage", color=Color.text_muted),
                spacing="0",
                align="start",
            ),
            spacing="4",
            align="center",
        ),
        rx.text(
            control_summary_display(entry),
            size="2",
            color=Color.text_muted,
            margin_top="1rem",
        ),
        rx.text(
            entry["provisional_reason"],
            size="2",
            color=Color.text_muted,
            margin_top="0.75rem",
            font_style="italic",
        )
        if entry["provisional_reason"]
        else rx.box(),
        border=BORDER,
        border_radius="12px",
        padding="1.5rem",
        background=Color.bg,
        margin_bottom="2rem",
    )


def _token_body(entry: dict) -> rx.Component:
    questions_by_name = {q["name"]: q for q in entry["questions"]}
    return rx.box(
        rx.link(
            "← Back to the scorecard",
            href="/projects/rwa-scorecard",
            color=Color.accent,
            font_weight="600",
            margin_bottom="1.5rem",
            display="inline-block",
        ),
        _token_header(entry),
        _overall_summary(entry),
        rx.box(
            *[question_detail_card(questions_by_name[name]) for name in QUESTION_ORDER],
            display="grid",
            grid_template_columns="1fr",
            gap="1rem",
        ),
        rx.link(
            "How we assess →",
            href="/projects/rwa-scorecard/how-we-assess",
            color=Color.accent,
            font_weight="600",
            margin_top="2rem",
            display="inline-block",
        ),
        width="100%",
        max_width=Spacing.content_max_width,
        margin="0 auto",
        padding_bottom=Spacing.section_gap,
    )


def _not_found() -> rx.Component:
    return rx.box(
        rx.heading("Asset not found", as_="h1", size="7"),
        rx.text(
            "We don't track an asset at this address yet.",
            color=Color.text_muted,
            margin_top="0.5rem",
        ),
        rx.link(
            "← Back to the scorecard",
            href="/projects/rwa-scorecard",
            color=Color.accent,
            font_weight="600",
            margin_top="1rem",
            display="inline-block",
        ),
        width="100%",
        max_width=Spacing.content_max_width,
        margin="0 auto",
        padding_bottom=Spacing.section_gap,
    )


def rwa_scorecard_token_page(entry: dict):
    """Return a zero-arg page function rendering this specific token."""

    def _page() -> rx.Component:
        return page_shell(_token_body(entry))

    return _page


def rwa_scorecard_token_not_found_page() -> rx.Component:
    """Catch-all for /projects/rwa-scorecard/<slug> when <slug> isn't a
    known token."""
    return page_shell(_not_found())
