"""Page shell: navbar + centered content column + footer."""

import reflex as rx

from ..theme import Color, FONT_FAMILY, Spacing
from .footer import footer
from .navbar import navbar


def page_shell(*children, max_width: str = Spacing.page_max_width) -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            *children,
            width="100%",
            max_width=max_width,
            margin="0 auto",
            padding_x=Spacing.page_padding_x,
            padding_top=Spacing.section_gap,
        ),
        footer(),
        width="100%",
        min_height="100vh",
        background=Color.bg,
        color=Color.text,
        font_family=FONT_FAMILY,
    )
