"""RWA Oracle Scorecard methodology page: static text + diagram, no backend."""

import reflex as rx

from ..components.layout import page_shell
from ..components.scorecard_methodology import how_we_assess_content
from ..theme import Color


def rwa_scorecard_how_we_assess() -> rx.Component:
    return page_shell(
        rx.link(
            "← Back to the scorecard",
            href="/projects/rwa-scorecard",
            color=Color.accent,
            font_weight="600",
            margin_bottom="1.5rem",
            display="inline-block",
        ),
        how_we_assess_content(),
    )
