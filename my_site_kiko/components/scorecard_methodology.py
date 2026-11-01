"""The RWA Oracle Scorecard's "How we assess" content, ported from the
scorecard repo's rwa_scorecard/pages/how_we_assess.py into the blog's own
theme. Static text + diagram, no State -- same content, new skin.
"""

import reflex as rx

from ..theme import BORDER, Color, RADIUS_MD, Spacing, bp

DEEP_QUESTIONS = [
    (
        "Is the data recent?",
        "Freshness",
        "If you ask a friend if it's raining and they tell you about last "
        "week, that doesn't help. We check how long it's been since the "
        "oracle last updated, against how often it's supposed to -- its "
        "age versus its expected heartbeat.",
        "clock",
    ),
    (
        "Do tokens = reserves?",
        "Supply vs. reserves",
        "If the coat check hands out 10 tickets but only has 8 coats, two "
        "people go home cold. We compare the tokens in circulation against "
        "the reserves the issuer says are backing them, and how old that "
        "attestation is.",
        "scale",
    ),
    (
        "Does the market believe the NAV?",
        "Price deviation",
        "If the receipt says the coat is worth $1,000 but people sell it for "
        "$800, they're worried about something. We check how far the market "
        "price trades from the stated net asset value.",
        "trending-down",
    ),
    (
        "Who could change the rules?",
        "Control",
        "If only one person holds the key to the coat-check register, they "
        "can rewrite any entry. We check how many independent keys it would "
        "take to change this asset's contract or its oracle, and whether "
        "oracle updates come from a healthy spread of sources rather than "
        "one.",
        "key",
    ),
]

QUESTION_PILL_LABELS = {
    "q1": "Q1 Freshness",
    "q2": "Q2 Supply vs reserves",
    "q3": "Q3 Price vs NAV",
    "q4": "Q4 Control",
}

DIAGRAM_STEPS = [
    (
        "landmark",
        "The coat",
        "Real asset · off-chain",
        "Dollars in a bank, treasuries at a custodian, gold in a vault.",
        ("q2",),
    ),
    (
        "radio-tower",
        "The messenger",
        "Oracle",
        "Tells the blockchain what's really in the back room.",
        ("q1", "q4"),
    ),
    (
        "ticket",
        "The receipt",
        "Token · on-chain",
        "What you actually hold.",
        ("q3", "q2"),
    ),
]


def _diagram_question_pills(qids: tuple[str, ...]) -> rx.Component:
    return rx.hstack(
        *[
            rx.link(
                rx.box(
                    QUESTION_PILL_LABELS[qid],
                    padding_x="0.6rem",
                    padding_y="0.2rem",
                    border_radius="999px",
                    background=Color.accent_soft,
                    color=Color.accent,
                    font_size="0.75rem",
                    font_weight="medium",
                ),
                href=f"#{qid}",
                text_decoration="none",
            )
            for qid in qids
        ],
        spacing="2",
        wrap="wrap",
        margin_top="0.75rem",
    )


def _diagram_box(icon: str, title: str, tag: str, text: str, qids: tuple[str, ...]) -> rx.Component:
    return rx.box(
        rx.icon(icon, color=Color.accent, size=26),
        rx.heading(title, size="4", margin_top="0.4em", color=Color.text),
        rx.text(
            tag,
            size="1",
            text_transform="uppercase",
            letter_spacing="0.08em",
            color=Color.text_faint,
            margin_top="0.2em",
        ),
        rx.text(text, color=Color.text_muted, margin_top="0.5em", size="2"),
        _diagram_question_pills(qids),
        background=Color.bg,
        border=BORDER,
        border_radius=RADIUS_MD,
        padding="1.25em",
        min_width="0",
        flex="1",
    )


def _diagram_arrow() -> rx.Component:
    return rx.box(
        rx.icon("arrow-right", color=Color.accent, size=22, display=bp("none", "none", "flex")),
        rx.icon("arrow-down", color=Color.accent, size=22, display=bp("flex", "flex", "none")),
        display="flex",
        align_items="center",
        justify_content="center",
        flex_shrink="0",
        padding="0.25em",
    )


def _diagram_divider() -> rx.Component:
    return rx.box(
        rx.text(
            "off-chain | on-chain",
            size="1",
            text_transform="uppercase",
            letter_spacing="0.05em",
            color=Color.text_faint,
            white_space="nowrap",
        ),
        border_left=bp("none", "none", f"2px dashed {Color.border_strong}"),
        border_top=bp(f"2px dashed {Color.border_strong}", f"2px dashed {Color.border_strong}", "none"),
        padding=bp("0.75em 0", "0.75em 0", "0 1em"),
        display="flex",
        align_items="center",
        justify_content="center",
        flex_shrink="0",
    )


def _coat_check_diagram() -> rx.Component:
    return rx.flex(
        _diagram_box(*DIAGRAM_STEPS[0]),
        _diagram_arrow(),
        _diagram_divider(),
        _diagram_box(*DIAGRAM_STEPS[1]),
        _diagram_arrow(),
        _diagram_box(*DIAGRAM_STEPS[2]),
        direction=bp("column", "column", "row"),
        align="stretch",
        wrap="nowrap",
        spacing="3",
        width="100%",
        margin_top="1em",
    )


def how_we_assess_content() -> rx.Component:
    return rx.box(
        rx.box(
            "METHODOLOGY · v0.1-draft",
            padding_x="0.6rem",
            padding_y="0.2rem",
            border_radius="999px",
            background=Color.accent_soft,
            color=Color.accent,
            font_size="0.75rem",
            font_weight="medium",
            display="inline-block",
        ),
        rx.heading(
            "How we assess",
            as_="h1",
            size=bp("6", "7", "8"),
            weight="bold",
            margin_top="0.5em",
        ),
        rx.text(
            "Every tokenized real-world asset makes the same basic promise: "
            "the thing on-chain tracks something real off-chain. We use a coat "
            "check as our mental model for that promise.",
            color=Color.text_muted,
            margin_top="0.75em",
            size="3",
            max_width=Spacing.content_max_width,
        ),
        rx.box(
            rx.heading("The coat check", size="5", margin_top="2em", color=Color.text),
            _coat_check_diagram(),
            rx.text(
                "The whole question comes down to whether the messenger is "
                "telling the truth, and whether you'd notice if they weren't.",
                color=Color.text_muted,
                margin_top="1em",
                text_align="center",
            ),
            background=Color.accent_soft,
            border=BORDER,
            border_radius=RADIUS_MD,
            padding="1.5em",
            margin_top="1em",
        ),
        rx.heading(
            "The four questions we ask every asset",
            size="5",
            margin_top="2.5em",
            color=Color.text,
        ),
        rx.box(
            *[
                rx.box(
                    rx.hstack(
                        rx.icon(icon, color=Color.accent, size=22),
                        rx.text(
                            f"Question {i + 1} · {label}",
                            size="1",
                            text_transform="uppercase",
                            letter_spacing="0.08em",
                            color=Color.text_faint,
                        ),
                        align="center",
                        spacing="2",
                    ),
                    rx.heading(q, size="4", margin_top="0.5em", color=Color.text),
                    rx.text(long, color=Color.text_muted, margin_top="0.5em", size="2"),
                    id=f"q{i + 1}",
                    border=BORDER,
                    border_radius=RADIUS_MD,
                    padding="1.5em",
                    background=Color.bg,
                )
                for i, (q, label, long, icon) in enumerate(DEEP_QUESTIONS)
            ],
            display="grid",
            grid_template_columns=bp("1fr", "1fr", "repeat(2, 1fr)"),
            gap="1.25rem",
            margin_top="1em",
        ),
        rx.text(
            "Each sub-score is 0-100 when we can measure it. A question "
            "that genuinely doesn't apply to an asset — price-vs-NAV for "
            "an allowlist-gated fund with no public market, say — is left "
            "out of its average entirely. But a question that does apply "
            "and simply isn't disclosed scores the same as a 0: "
            "disclosing less isn't a free pass to a higher average. The "
            "coverage percentage next to the overall score shows how many "
            "of the applicable questions we actually have data for.",
            color=Color.text_muted,
            margin_top="2em",
            max_width=Spacing.content_max_width,
        ),
        rx.text(
            "Q4 currently counts keys only; timelocks and mint caps will be "
            "weighted in a future version.",
            color=Color.text_muted,
            margin_top="1em",
            font_style="italic",
            max_width=Spacing.content_max_width,
        ),
        width="100%",
        padding_bottom=Spacing.section_gap,
    )
