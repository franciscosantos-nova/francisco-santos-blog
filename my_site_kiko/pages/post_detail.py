"""Individual post pages, one static route per post slug.

Each post gets its own page registered at /posts/<slug> (see
my_site_kiko.py), with its content baked in at build time — no
dependency on State, so it works without a live backend. The dynamic
/posts/[slug] route is kept only as a catch-all for slugs that don't
match any known post.
"""

import reflex as rx

from ..components.layout import page_shell
from ..theme import Color, RADIUS_MD, Spacing
from ..utils.posts import Post


def _tag_pill(tag: str) -> rx.Component:
    return rx.box(
        rx.text(tag, size="1", weight="medium", color=Color.accent),
        padding_x="0.6rem",
        padding_y="0.2rem",
        border_radius="999px",
        background=Color.accent_soft,
    )


def _post_body(post: Post) -> rx.Component:
    return rx.box(
        rx.box(
            rx.flex(
                *[_tag_pill(t) for t in post.tags],
                gap="0.5rem",
                margin_bottom="1rem",
                wrap="wrap",
            )
            if post.tags
            else None,
            rx.heading(
                post.title,
                as_="h1",
                size="8",
                weight="bold",
                line_height="1.15",
                margin_bottom="0.75rem",
            ),
            rx.text(post.date_display, size="2", color=Color.text_faint),
            margin_bottom="2rem",
        ),
        rx.image(
            src=post.cover,
            width="100%",
            max_height="420px",
            object_fit="cover",
            border_radius=RADIUS_MD,
            margin_bottom="2.5rem",
        )
        if post.cover
        else None,
        rx.markdown(
            post.content,
            component_map={
                "img": lambda value: rx.image(
                    value,
                    width="100%",
                    border_radius=RADIUS_MD,
                    margin_y="1.5em",
                ),
                "blockquote": lambda value: rx.box(
                    value,
                    border_left=f"3px solid {Color.accent}",
                    padding_left="1.25rem",
                    margin_y="1.5em",
                    color=Color.text_muted,
                    font_style="italic",
                ),
            },
        ),
        width="100%",
        max_width=Spacing.content_max_width,
        margin="0 auto",
        padding_bottom=Spacing.section_gap,
    )


def _not_found() -> rx.Component:
    return rx.box(
        rx.heading("Post not found", as_="h1", size="7"),
        rx.link("← Back to posts", href="/posts", color=Color.accent),
        width="100%",
        max_width=Spacing.content_max_width,
        margin="0 auto",
        padding_bottom=Spacing.section_gap,
    )


def post_page(post: Post):
    """Return a zero-arg page function rendering this specific post."""

    def _page() -> rx.Component:
        return page_shell(_post_body(post))

    return _page


def post_not_found_page() -> rx.Component:
    """Catch-all for /posts/<slug> when <slug> isn't a known post."""
    return page_shell(_not_found())
