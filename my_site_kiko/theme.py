"""Central design tokens: colors, fonts and spacing.

Keeping these in one place means the look of the whole site can be tuned
from a single file.
"""

FONT_FAMILY = "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"

GOOGLE_FONT_STYLESHEET = (
    "https://fonts.googleapis.com/css2?"
    "family=Inter:wght@400;500;600;700;800&display=swap"
)


class Color:
    """Flat color palette — light theme, single deep-blue accent."""

    accent = "#1E3A8A"
    accent_hover = "#162C6B"
    accent_soft = "#EEF2FC"

    bg = "#FFFFFF"
    bg_subtle = "#FAFAFA"

    text = "#111318"
    text_muted = "#5B5F6B"
    text_faint = "#9094A0"

    border = "#E7E8EC"
    border_strong = "#D4D6DC"


class Spacing:
    """Shared layout measurements."""

    page_max_width = "1120px"
    content_max_width = "720px"
    page_padding_x = "1.5rem"

    section_gap = "clamp(3rem, 8vw, 6rem)"


RADIUS_SM = "8px"
RADIUS_MD = "12px"
RADIUS_LG = "20px"

BORDER = f"1px solid {Color.border}"


def bp(*values):
    """Build a responsive value from positional breakpoints.

    bp("a", "b", "c") == initial="a" (mobile), sm="b" (tablet), md="c" (desktop).
    """
    import reflex as rx

    keys = ["initial", "sm", "md", "lg", "xl"]
    return rx.breakpoints(**{k: v for k, v in zip(keys, values) if v is not None})
