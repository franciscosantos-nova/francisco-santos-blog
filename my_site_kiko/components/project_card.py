"""Card used on the /projects page."""

import reflex as rx

from ..theme import BORDER, Color, RADIUS_MD


def _tag_pill(tag: str) -> rx.Component:
    return rx.box(
        rx.text(tag, size="1", weight="medium", color=Color.accent),
        padding_x="0.6rem",
        padding_y="0.2rem",
        border_radius="999px",
        background=Color.accent_soft,
    )


def _coat_check_step(icon: str, label: str) -> rx.Component:
    return rx.vstack(
        rx.icon(icon, color=Color.accent, size=26),
        rx.text(
            label,
            size="1",
            weight="medium",
            text_transform="uppercase",
            letter_spacing="0.06em",
            color=Color.accent,
            margin_top="0.3rem",
        ),
        spacing="0",
        align="center",
    )


def _coat_check_arrow() -> rx.Component:
    return rx.icon("arrow-right", color=Color.accent, size=18, margin_bottom="1.4rem")


def _coat_check_header() -> rx.Component:
    return rx.box(
        rx.hstack(
            _coat_check_step("landmark", "Asset"),
            _coat_check_arrow(),
            _coat_check_step("radio-tower", "Oracle"),
            _coat_check_arrow(),
            _coat_check_step("ticket", "Token"),
            align="start",
            justify="center",
            spacing="3",
        ),
        width="100%",
        height="180px",
        background=Color.bg_subtle,
        border_radius=f"{RADIUS_MD} {RADIUS_MD} 0 0",
        display="flex",
        align_items="center",
        justify_content="center",
    )


def _project_header(project: dict) -> rx.Component | None:
    if project.get("header") == "coat_check":
        return _coat_check_header()
    if project["image"]:
        return rx.box(
            rx.image(
                src=project["image"],
                width="100%",
                height="180px",
                object_fit=project.get("image_fit", "cover"),
                padding="1.5rem" if project.get("image_fit") == "contain" else "0",
            ),
            width="100%",
            background=Color.bg_subtle if project.get("image_fit") == "contain" else None,
            border_radius=f"{RADIUS_MD} {RADIUS_MD} 0 0",
            overflow="hidden",
        )
    return None


def project_card(project: dict) -> rx.Component:
    return rx.link(
        rx.box(
            _project_header(project),
            rx.box(
                rx.heading(
                    project["title"],
                    as_="h3",
                    size="4",
                    margin_bottom="0.5rem",
                    color=Color.text,
                ),
                rx.text(project["description"], size="2", color=Color.text_muted),
                rx.flex(
                    *[_tag_pill(t) for t in project["tags"]],
                    gap="0.5rem",
                    margin_top="0.9rem",
                    wrap="wrap",
                )
                if project["tags"]
                else None,
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
        href=project["href"],
        is_external=project["is_external"],
        text_decoration="none",
        width="100%",
        height="100%",
        display="block",
    )
