"""App entry point: creates the Reflex App and registers every route."""

import reflex as rx

from .config import SITE
from .data.rwa_scorecard import ALL_TOKENS
from .pages.index import index
from .pages.journey import journey
from .pages.post_detail import post_not_found_page, post_page
from .pages.posts import posts
from .pages.projects import projects
from .pages.rwa_scorecard import rwa_scorecard
from .pages.rwa_scorecard_how_we_assess import rwa_scorecard_how_we_assess
from .pages.rwa_scorecard_token import (
    rwa_scorecard_token_not_found_page,
    rwa_scorecard_token_page,
)
from .theme import Color, FONT_FAMILY, GOOGLE_FONT_STYLESHEET
from .utils.posts import get_all_posts

app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="blue",
        gray_color="slate",
        radius="large",
        scaling="100%",
    ),
    style={
        "font_family": FONT_FAMILY,
        "background_color": Color.bg,
        "color": Color.text,
    },
    stylesheets=[GOOGLE_FONT_STYLESHEET],
)
# This site has no State anywhere, so it never needs a live backend
# connection -- but Reflex's default "Overlay" app-wrap still renders a
# connection-error banner/pulser whenever it can't open the websocket,
# which is always true for a static export served with no backend at all.
# There's no `overlay_component` App field in this Reflex version (0.9.12);
# the equivalent is overriding the "Overlay" entry in app_wraps directly.
app.app_wraps[5, "Overlay"] = lambda stateful: None

app.add_page(index, route="/", title=f"{SITE['name']} — {SITE['role']}")
app.add_page(journey, route="/journey", title=f"Journey — {SITE['name']}")
app.add_page(posts, route="/posts", title=f"Posts — {SITE['name']}")
for _post in get_all_posts():
    app.add_page(
        post_page(_post),
        route=f"/posts/{_post.slug}",
        title=f"{_post.title} — {SITE['name']}",
    )
app.add_page(
    post_not_found_page, route="/posts/[slug]", title=f"Post — {SITE['name']}"
)
app.add_page(projects, route="/projects", title=f"Projects — {SITE['name']}")
app.add_page(
    rwa_scorecard,
    route="/projects/rwa-scorecard",
    title=f"RWA Oracle Scorecard — {SITE['name']}",
)
app.add_page(
    rwa_scorecard_how_we_assess,
    route="/projects/rwa-scorecard/how-we-assess",
    title=f"How We Assess — RWA Oracle Scorecard — {SITE['name']}",
)
for _entry in ALL_TOKENS:
    app.add_page(
        rwa_scorecard_token_page(_entry),
        route=f"/projects/rwa-scorecard/{_entry['slug']}",
        title=f"{_entry['symbol']} — RWA Oracle Scorecard — {SITE['name']}",
    )
app.add_page(
    rwa_scorecard_token_not_found_page,
    route="/projects/rwa-scorecard/[slug]",
    title=f"Asset — RWA Oracle Scorecard — {SITE['name']}",
)
