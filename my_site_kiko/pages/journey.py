"""Journey page: vertical milestone timeline."""

import reflex as rx

from ..components.layout import page_shell
from ..components.timeline_item import timeline_item
from ..data.journey import MILESTONES
from ..theme import Color, Spacing, bp


def journey() -> rx.Component:
    return page_shell(
        rx.box(
            rx.heading(
                "My journey",
                as_="h1",
                size=bp("6", "7", "8"),
                weight="bold",
                margin_bottom="0.75rem",
            ),
            rx.text(
                "Milestones on the way to becoming an expert in RWA tokenization "
                "and on-chain finance.",
                size=bp("3", "3", "4"),
                color=Color.text_muted,
                max_width=Spacing.content_max_width,
            ),
            margin_bottom="3rem",
        ),
        rx.box(
            *[
                timeline_item(m, is_last=(i == len(MILESTONES) - 1))
                for i, m in enumerate(MILESTONES)
            ],
            width="100%",
            max_width=Spacing.content_max_width,
            padding_bottom=Spacing.section_gap,
        ),
    )
