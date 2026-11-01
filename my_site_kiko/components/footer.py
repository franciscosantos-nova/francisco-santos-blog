"""Site footer, shared by every page."""

import reflex as rx

from ..config import SITE
from ..theme import BORDER, Color, Spacing, bp


def _footer_link(label: str, href: str) -> rx.Component:
    return rx.link(
        label,
        href=href,
        is_external=True,
        size="2",
        color=Color.text_muted,
        text_decoration="none",
        _hover={"color": Color.accent},
    )


def footer() -> rx.Component:
    social = SITE["social"]
    return rx.box(
        rx.flex(
            rx.text(
                f"© {SITE['name']}",
                size="2",
                color=Color.text_faint,
            ),
            rx.spacer(),
            rx.flex(
                _footer_link("LinkedIn", social["linkedin"]),
                _footer_link("GitHub", social["github"]),
                _footer_link("Email", f"mailto:{SITE['email']}"),
                gap="1.5rem",
                align="center",
                wrap="wrap",
            ),
            align="center",
            justify="between",
            width="100%",
            direction=bp("column", "column", "row"),
            gap=bp("1.25rem", "1.25rem", "0"),
        ),
        width="100%",
        max_width=Spacing.page_max_width,
        margin="0 auto",
        padding_x=Spacing.page_padding_x,
        padding_y="2.5rem",
        border_top=BORDER,
        margin_top=Spacing.section_gap,
    )
