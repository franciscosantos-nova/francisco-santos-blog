"""RWA Oracle Scorecard ranking page: a static snapshot, no live backend.

Data comes from data/rwa_scorecard.py, which reads the JSON exported by the
separate rwa-oracle-scorecard repo's export_snapshot script. Everything
here is plain Python resolved at build time, same pattern as the Dune
dashboards and blog posts pages.
"""

import reflex as rx

from ..components.layout import page_shell
from ..components.scorecard_cards import asset_card, provisional_asset_card
from ..data.rwa_scorecard import (
    METHODOLOGY_VERSION,
    PROVISIONAL,
    RANKING,
    generated_at_display,
)
from ..theme import BORDER, Color, Spacing, bp


def _footer_note() -> rx.Component:
    return rx.box(
        rx.text(
            f"Independent student project. Methodology {METHODOLOGY_VERSION or 'unknown'}. "
            "Scores measure data transparency, not solvency. Not investment advice. "
            f"Data as of {generated_at_display()}.",
            size="1",
            color=Color.text_faint,
        ),
        border_top=BORDER,
        padding_top="1.25rem",
        margin_top=Spacing.section_gap,
    )


def rwa_scorecard() -> rx.Component:
    return page_shell(
        rx.link(
            "← Back to Projects",
            href="/projects",
            color=Color.accent,
            font_weight="600",
            margin_bottom="1.5rem",
            display="inline-block",
        ),
        rx.box(
            rx.heading(
                "RWA Oracle Scorecard",
                as_="h1",
                size=bp("6", "7", "8"),
                weight="bold",
                margin_bottom="0.75rem",
            ),
            rx.text(
                "How verifiable is the on-chain data behind tokenized real-world "
                "assets? Ranked by how transparent and verifiable each asset's "
                "data is, across four questions: freshness, supply vs. "
                "reserves, price vs. NAV, and who controls it.",
                size=bp("3", "3", "4"),
                color=Color.text_muted,
                max_width=Spacing.content_max_width,
            ),
            rx.link(
                "How we assess →",
                href="/projects/rwa-scorecard/how-we-assess",
                size="2",
                color=Color.accent,
                font_weight="600",
                margin_top="0.5rem",
                display="inline-block",
            ),
            margin_bottom="2.5rem",
        ),
        rx.box(
            rx.box(
                *[
                    asset_card(entry, rank=i + 1)
                    for i, entry in enumerate(RANKING)
                ]
                if RANKING
                else [
                    rx.text(
                        "No asset has been ranked yet.",
                        size="3",
                        color=Color.text_muted,
                    )
                ],
                display="grid",
                grid_template_columns=bp("1fr", "1fr", "repeat(3, 1fr)"),
                gap="1.25rem",
                width="100%",
            ),
            rx.box(
                rx.heading(
                    "Provisional, not ranked yet",
                    as_="h2",
                    size="5",
                    weight="bold",
                    margin_bottom="0.5rem",
                ),
                rx.text(
                    "We could not yet verify enough about these assets to rank "
                    "them against the ones above.",
                    size="2",
                    color=Color.text_muted,
                    margin_bottom="1.25rem",
                ),
                rx.box(
                    *[provisional_asset_card(entry) for entry in PROVISIONAL],
                    display="grid",
                    grid_template_columns=bp("1fr", "1fr", "repeat(3, 1fr)"),
                    gap="1.25rem",
                    width="100%",
                ),
                margin_top="2.5rem",
            )
            if PROVISIONAL
            else rx.box(),
            _footer_note(),
            width="100%",
            padding_bottom=Spacing.section_gap,
        ),
    )
