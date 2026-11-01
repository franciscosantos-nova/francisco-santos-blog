"""Journey timeline milestones — newest first.

Add a new milestone by appending a dict at the top of MILESTONES. Leave
"date" as "TODO" until the real date is known. Do not invent dates.

Each milestone supports:
    date: str            e.g. "2026-03" or "TODO"
    title: str
    description: str
    image: str | None     path under assets/, e.g. "/images/foo.jpg"
"""

MILESTONES = [
    {
        "date": "TODO",
        "title": "Incoming exchange semester at HKUST",
        "description": (
            "Heading to the Hong Kong University of Science and Technology "
            "(HKUST) for an exchange semester."
        ),
        "image": "/images/hong_kong.jpg",
    },
    {
        "date": "TODO",
        "title": "Started writing about RWA",
        "description": (
            "Began publishing writing on Real World Asset tokenization and "
            "on-chain finance as a way to learn in public."
        ),
        "image": None,
    },
    {
        "date": "TODO",
        "title": "Research at Wonder Payment (Hong Kong fintech)",
        "description": "Remote research work for Wonder Payment, a Hong Kong-based fintech.",
        "image": "/images/wonder_payment.jpg",
    },
    {
        "date": "TODO",
        "title": "Audit summer internship at PwC Portugal",
        "description": "Summer internship in the Audit practice at PwC Portugal.",
        "image": "/images/pwc_internship.jpeg",
    },
    {
        "date": "TODO",
        "title": "Built NovaExchange",
        "description": (
            "Built NovaExchange, an international mobility platform written in "
            "Python, funded by the Haddad Institute and implemented at Nova SU "
            "(novaexchange.eu)."
        ),
        "image": "/images/prototypingnovaexchange.jpg",
    },
    {
        "date": "TODO",
        "title": "Joined Nova SBE",
        "description": (
            "Started my studies at Nova School of Business and Economics, "
            "the starting point of the path into finance and technology."
        ),
        "image": "/images/nova_sbe.jpg",
    },
]
