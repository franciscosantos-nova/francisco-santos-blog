"""Home page."""

import reflex as rx

from ..components.layout import page_shell
from ..components.post_card import post_card
from ..config import SITE
from ..theme import Color, RADIUS_MD, Spacing, bp
from ..utils.posts import get_all_posts


def _hero() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.text(
                SITE["role"],
                size=bp("2", "2", "2"),
                weight="bold",
                color=Color.accent,
                text_transform="uppercase",
                letter_spacing="0.06em",
            ),
            rx.heading(
                SITE["name"],
                as_="h1",
                size=bp("7", "8", "9"),
                weight="bold",
                margin_top="0.75rem",
                margin_bottom="1rem",
                letter_spacing="-0.02em",
                line_height="1.05",
            ),
            rx.text(
                SITE["tagline"],
                size=bp("3", "4", "5"),
                color=Color.text_muted,
                max_width="34rem",
                margin_bottom="2rem",
            ),
            rx.link(
                rx.button(
                    "Read my latest post",
                    size="3",
                    background=Color.accent,
                    color="white",
                    border_radius=RADIUS_MD,
                    _hover={"background": Color.accent_hover},
                ),
                href=(
                    f"/posts/{get_all_posts()[0].slug}"
                    if get_all_posts()
                    else "/posts"
                ),
            ),
            direction="column",
            align=bp("center", "center", "start"),
            text_align=bp("center", "center", "left"),
            flex="1",
        ),
        rx.image(
            src=SITE["profile_image"],
            width=bp("140px", "180px", "260px"),
            height=bp("140px", "180px", "260px"),
            object_fit="cover",
            border_radius="50%",
            margin_left=bp("0", "0", "3rem"),
            margin_bottom=bp("1.5rem", "1.75rem", "0"),
        ),
        width="100%",
        align="center",
        direction=bp("column-reverse", "column-reverse", "row"),
        justify="between",
        padding_bottom=Spacing.section_gap,
    )


def _about() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text(
                "About me",
                size="2",
                weight="bold",
                color=Color.accent,
                text_transform="uppercase",
                letter_spacing="0.06em",
            ),
            width=bp("100%", "100%", "240px"),
            min_width=bp("auto", "auto", "240px"),
            margin_bottom=bp("1rem", "1rem", "0"),
        ),
        rx.text(
            SITE["about"],
            size=bp("3", "3", "4"),
            color=Color.text_muted,
            line_height="1.7",
        ),
        width="100%",
        direction=bp("column", "column", "row"),
        gap="2rem",
        padding_y=Spacing.section_gap,
        border_top=f"1px solid {Color.border}",
    )


def _latest_posts() -> rx.Component:
    posts = get_all_posts()[:3]
    return rx.box(
        rx.flex(
            rx.heading("Latest posts", as_="h2", size=bp("6", "6", "7"), color=Color.text),
            rx.spacer(),
            rx.link(
                "All posts →",
                href="/posts",
                size="3",
                color=Color.accent,
                text_decoration="none",
                weight="medium",
            ),
            width="100%",
            align="center",
            margin_bottom="1.75rem",
        ),
        rx.grid(
            *[post_card(p) for p in posts],
            columns=bp("1", "1", "3"),
            gap="1.5rem",
            width="100%",
        )
        if posts
        else rx.text("No posts yet.", color=Color.text_muted),
        width="100%",
        padding_y=Spacing.section_gap,
        border_top=f"1px solid {Color.border}",
    )


def index() -> rx.Component:
    return page_shell(
        _hero(),
        _about(),
        _latest_posts(),
    )
