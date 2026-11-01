"""Prepends our own Cloudflare Pages redirects to the _redirects file Reflex's
export generates in .web/build/client/ (a plain `/* /index.html 200` SPA
fallback rule). Cloudflare evaluates _redirects top-to-bottom and uses the
first match, so our specific 301s must come before that catch-all -- run
this after every `reflex export`, before deploying.
"""

from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parents[1] / ".web" / "build" / "client"
REDIRECTS_PATH = BUILD_DIR / "_redirects"

OUR_RULES = (
    "/dashboards              /projects              301\n"
    "/dashboards/*            /projects/:splat        301\n"
)


def main() -> int:
    if not REDIRECTS_PATH.exists():
        print(f"error: {REDIRECTS_PATH} does not exist -- run `reflex export` first")
        return 1

    existing = REDIRECTS_PATH.read_text(encoding="utf-8")
    if OUR_RULES in existing:
        print(f"{REDIRECTS_PATH} already has our redirect rules, nothing to do")
        return 0

    REDIRECTS_PATH.write_text(OUR_RULES + existing, encoding="utf-8")
    print(f"prepended /dashboards -> /projects redirects to {REDIRECTS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
