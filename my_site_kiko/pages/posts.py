"""Posts index page: grid of all post cards."""

import reflex as rx

from ..components.layout import page_shell
from ..components.post_card import post_card
from ..theme import Color, Spacing, bp
from ..utils.posts import get_all_posts


def posts() -> rx.Component:
    all_posts = get_all_posts()
    return page_shell(
        rx.box(
            rx.heading(
                "Posts",
                as_="h1",
                size=bp("6", "7", "8"),
                weight="bold",
                margin_bottom="0.75rem",
            ),
            rx.text(
                "Writing on RWA tokenization, on-chain finance and what I'm "
                "learning along the way.",
                size=bp("3", "3", "4"),
                color=Color.text_muted,
                max_width=Spacing.content_max_width,
            ),
            margin_bottom="3rem",
        ),
        rx.box(
            rx.grid(
                *[post_card(p) for p in all_posts],
                columns=bp("1", "1", "3"),
                gap="1.5rem",
                width="100%",
            )
            if all_posts
            else rx.text(
                "No posts yet — add a .md file to /posts.", color=Color.text_muted
            ),
            padding_bottom=Spacing.section_gap,
        ),
    )
