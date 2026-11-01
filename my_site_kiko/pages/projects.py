"""Projects page: things I've built."""

import reflex as rx

from ..components.layout import page_shell
from ..components.project_card import project_card
from ..data.projects import PROJECTS
from ..theme import Spacing, bp


def projects() -> rx.Component:
    return page_shell(
        rx.box(
            rx.heading(
                "Projects",
                as_="h1",
                size=bp("6", "7", "8"),
                weight="bold",
                margin_bottom="0.75rem",
            ),
            margin_bottom="2.5rem",
        ),
        rx.box(
            rx.box(
                *[project_card(p) for p in PROJECTS],
                display="grid",
                grid_template_columns=bp("1fr", "1fr", "repeat(2, 1fr)"),
                gap="1.5rem",
                width="100%",
            ),
            width="100%",
            padding_bottom=Spacing.section_gap,
        ),
    )
