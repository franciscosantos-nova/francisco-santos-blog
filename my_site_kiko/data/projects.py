"""Projects shown on the /projects page.

Each entry supports:
    title: str
    description: str
    tags: list[str]
    image: str | None     path under assets/, e.g. "/images/foo.jpg"
    image_fit: str        "cover" (default, for photos) or "contain" (for
                           a logo that shouldn't be cropped)
    header: str            "image" (default) or "coat_check" -- a drawn
                           header (no image file) for the RWA Scorecard card
    href: str             external URL or internal route
    is_external: bool     True opens in a new tab with rel=noopener
"""

PROJECTS = [
    {
        "title": "NovaExchange",
        "description": (
            "An international mobility platform written in Python, funded by "
            "the Haddad Institute and implemented at Nova SU."
        ),
        "tags": [],
        "image": "/images/novaexchangeupdatedlogo.png",
        "image_fit": "contain",
        "href": "https://novaexchange.eu",
        "is_external": True,
    },
    {
        "title": "RWA Oracle Scorecard",
        "description": "How verifiable is the on-chain data of tokenized assets?",
        "tags": ["7 tokens", "v0.1-draft"],
        "image": None,
        "header": "coat_check",
        "href": "/projects/rwa-scorecard",
        "is_external": False,
    },
]
