"""Card used to preview a post on the home and posts pages."""

import reflex as rx

from ..theme import BORDER, Color, RADIUS_MD
from ..utils.posts import Post


def _tag_pill(tag: str) -> rx.Component:
    return rx.box(
        rx.text(tag, size="1", weight="medium", color=Color.accent),
        padding_x="0.6rem",
        padding_y="0.2rem",
        border_radius="999px",
        background=Color.accent_soft,
    )


def post_card(post: Post) -> rx.Component:
    return rx.link(
        rx.box(
            rx.box(
                rx.image(
                    src=post.cover or "/images/example-cover.jpg",
                    width="100%",
                    height="180px",
                    object_fit="cover",
                    border_radius=f"{RADIUS_MD} {RADIUS_MD} 0 0",
                ),
                width="100%",
                overflow="hidden",
            ),
            rx.box(
                rx.text(post.date_display, size="1", color=Color.text_faint),
                rx.heading(
                    post.title,
                    as_="h3",
                    size="4",
                    margin_top="0.4rem",
                    margin_bottom="0.5rem",
                    color=Color.text,
                ),
                rx.text(
                    post.excerpt,
                    size="2",
                    color=Color.text_muted,
                    style={
                        "display": "-webkit-box",
                        "WebkitLineClamp": "3",
                        "WebkitBoxOrient": "vertical",
                        "overflow": "hidden",
                    },
                ),
                rx.flex(
                    *[_tag_pill(t) for t in post.tags],
                    gap="0.5rem",
                    margin_top="0.9rem",
                    wrap="wrap",
                ),
                padding="1.25rem",
                flex="1",
                display="flex",
                flex_direction="column",
            ),
            width="100%",
            height="100%",
            display="flex",
            flex_direction="column",
            border=BORDER,
            border_radius=RADIUS_MD,
            overflow="hidden",
            background=Color.bg,
            style={"transition": "border-color 0.15s ease"},
            _hover={"border_color": Color.accent},
        ),
        href=f"/posts/{post.slug}",
        text_decoration="none",
        width="100%",
        height="100%",
        display="block",
    )
