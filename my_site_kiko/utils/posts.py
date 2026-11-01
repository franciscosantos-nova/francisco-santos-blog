"""Loads blog posts from markdown files in /posts.

Adding a post is just adding a new .md file to /posts with frontmatter —
no code changes needed. See posts/example-post.md for the expected shape.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, field
from pathlib import Path

import frontmatter

POSTS_DIR = Path(__file__).resolve().parents[2] / "posts"

_FALLBACK_DATE = dt.date.min


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    date: dt.date
    date_display: str
    excerpt: str
    tags: list[str]
    cover: str | None
    content: str
    is_draft: bool = False


def _parse_date(value) -> tuple[dt.date, str]:
    """Return (sortable_date, display_string) for a frontmatter date value."""
    if isinstance(value, dt.datetime):
        d = value.date()
        return d, d.isoformat()
    if isinstance(value, dt.date):
        return value, value.isoformat()
    if isinstance(value, str) and value.strip():
        try:
            d = dt.date.fromisoformat(value.strip())
            return d, d.isoformat()
        except ValueError:
            return _FALLBACK_DATE, value.strip()
    return _FALLBACK_DATE, "TODO"


def _normalize_tags(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [t.strip() for t in value.split(",") if t.strip()]
    return [str(t).strip() for t in value]


def _load_post(path: Path) -> Post:
    post = frontmatter.load(path)
    meta = post.metadata

    slug = str(meta.get("slug") or path.stem)
    date_value, date_display = _parse_date(meta.get("date"))

    return Post(
        slug=slug,
        title=str(meta.get("title", path.stem)),
        date=date_value,
        date_display=date_display,
        excerpt=str(meta.get("excerpt", "")),
        tags=_normalize_tags(meta.get("tags")),
        cover=meta.get("cover") or None,
        content=post.content,
        is_draft=bool(meta.get("draft", False)),
    )


def _load_all_posts() -> list[Post]:
    if not POSTS_DIR.exists():
        return []
    posts = [_load_post(p) for p in sorted(POSTS_DIR.glob("*.md"))]
    posts.sort(key=lambda p: p.date, reverse=True)
    return posts


ALL_POSTS: list[Post] = _load_all_posts()


def get_all_posts() -> list[Post]:
    return ALL_POSTS


def get_post_by_slug(slug: str) -> Post | None:
    for post in ALL_POSTS:
        if post.slug == slug:
            return post
    return None
