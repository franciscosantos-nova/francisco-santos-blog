"""Loads the RWA Oracle Scorecard's static snapshot from /data/rwa_scorecard.json.

The snapshot is produced by a separate repo (rwa-oracle-scorecard)'s
``python -m scorecard_data.export_snapshot`` and copied in here by hand (for
now) at ``data/rwa_scorecard.json``, one directory above this package. Read
once at import time, like utils/posts.py -- no backend, no live requests.
"""

from __future__ import annotations

import json
from pathlib import Path

SNAPSHOT_PATH = Path(__file__).resolve().parents[2] / "data" / "rwa_scorecard.json"


def _load_snapshot() -> dict:
    if not SNAPSHOT_PATH.exists():
        return {"generated_at": None, "methodology_version": None, "tokens": []}
    return json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))


_SNAPSHOT = _load_snapshot()

GENERATED_AT: str | None = _SNAPSHOT.get("generated_at")
METHODOLOGY_VERSION: str | None = _SNAPSHOT.get("methodology_version")
ALL_TOKENS: list[dict] = _SNAPSHOT.get("tokens", [])

RANKING: list[dict] = sorted(
    (t for t in ALL_TOKENS if t["is_ranked"]),
    key=lambda t: t["overall_score"] or 0,
    reverse=True,
)

PROVISIONAL: list[dict] = sorted(
    (t for t in ALL_TOKENS if not t["is_ranked"]),
    key=lambda t: t["symbol"],
)


def format_iso_utc(iso: str | None) -> str:
    """"2026-11-01T17:48:34.096103+00:00" -> "2026-11-01 17:48 UTC"."""
    if not iso:
        return "unknown"
    date_part, time_part = iso.split("T")
    return f"{date_part} {time_part[:5]} UTC"


def generated_at_display() -> str:
    return format_iso_utc(GENERATED_AT)
