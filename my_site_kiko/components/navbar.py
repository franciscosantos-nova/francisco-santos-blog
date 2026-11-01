"""Top navigation bar, shared by every page."""

import reflex as rx

from ..config import SITE
from ..theme import BORDER, Color, Spacing, bp

NAV_LINKS = [
    ("Home", "/"),
    ("Journey", "/journey"),
    ("Posts", "/posts"),
    ("Projects", "/projects"),
]


def _nav_link(label: str, href: str) -> rx.Component:
    # Deliberately no current-page highlight here: that needs
    # rx.State.router.page.path, which requires a live backend connection
    # to sync -- this site is fully static (no State anywhere), and a
    # connection the export can't make just shows a "disconnected" banner
    # on every page for no benefit.
    return rx.link(
        label,
        href=href,
        size="3",
        weight="medium",
        color=Color.text_muted,
        text_decoration="none",
        _hover={"color": Color.accent},
        style={"transition": "color 0.15s ease"},
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.link(
                SITE["name"],
                href="/",
                size="4",
                weight="bold",
                color=Color.text,
                text_decoration="none",
                letter_spacing="-0.01em",
            ),
            rx.spacer(),
            rx.flex(
                *[_nav_link(label, href) for label, href in NAV_LINKS],
                gap=bp("1.1rem", "1.5rem", "2rem"),
                align="center",
                justify="center",
                wrap="wrap",
            ),
            align="center",
            width="100%",
            direction=bp("column", "column", "row"),
            gap=bp("1rem", "1rem", "0"),
        ),
        width="100%",
        max_width=Spacing.page_max_width,
        margin="0 auto",
        padding_x=Spacing.page_padding_x,
        padding_y="1.5rem",
        border_bottom=BORDER,
    )
