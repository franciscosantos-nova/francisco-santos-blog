"""A single milestone row on the /journey timeline."""

import reflex as rx

from ..theme import Color, RADIUS_SM


def timeline_item(milestone: dict, is_last: bool = False) -> rx.Component:
    rail_children = [
        rx.box(
            width="10px",
            height="10px",
            min_height="10px",
            border_radius="50%",
            background=Color.accent,
            margin_top="0.35rem",
        ),
    ]
    if not is_last:
        rail_children.append(
            rx.box(flex="1", width="2px", background=Color.border, margin_top="0.3rem")
        )

    content_children = [
        rx.text(milestone["date"], size="2", color=Color.text_faint, weight="medium"),
        rx.heading(
            milestone["title"],
            as_="h3",
            size="5",
            margin_top="0.3rem",
            margin_bottom="0.5rem",
            color=Color.text,
        ),
        rx.text(milestone["description"], size="3", color=Color.text_muted),
    ]
    if milestone.get("image"):
        content_children.append(
            rx.image(
                src=milestone["image"],
                width="100%",
                max_width="420px",
                border_radius=RADIUS_SM,
                margin_top="1rem",
            )
        )

    return rx.flex(
        rx.box(
            *rail_children,
            display="flex",
            flex_direction="column",
            align_items="center",
            width="24px",
            min_width="24px",
            margin_right="1.5rem",
        ),
        rx.box(
            *content_children,
            padding_bottom="2.75rem",
        ),
        width="100%",
    )
