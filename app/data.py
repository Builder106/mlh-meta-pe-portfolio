"""Single source of truth for the portfolio's content.

This is a *pod* portfolio: a fleet of services, one per teammate. The landing
page lists every member; each member gets their own page at ``/u/<handle>``
automatically, and the menu bar grows a tab per member. Add a dict to
``MEMBERS`` (and drop an avatar) and you appear everywhere — no template or
route changes needed.

ADDING YOURSELF (teammates): copy MEMBER_TEMPLATE at the bottom into MEMBERS,
fill it in, and drop a square photo at app/static/img/<your-handle>.jpg.
"""

# --------------------------------------------------------------------------- #
# Pod — the "fleet" this status page describes.
# --------------------------------------------------------------------------- #
POD = {
    "name": "26.SUM.B.6",
    "label": "MLH × Meta — Production Engineering pod",
    "cohort": "26.SUM.B",
    "region": "us-east-1",
    "status": "OPERATIONAL",
    "tagline": "Our MLH × Meta Production Engineering pod — a small portfolio "
               "for each of us. Pick a name to see their page.",
    "repo": "https://github.com/Builder106/MLH-Meta-PE-Portfolio",
}

# --------------------------------------------------------------------------- #
# Members — one "service" per teammate. Order here = order on the fleet page.
# --------------------------------------------------------------------------- #
MEMBERS = [
    {
        "handle": "olayinka-vaughan",
        "name": "Olayinka Vaughan",
        "github": "Builder106",
        "role": "Production Engineering Fellow",
        "status": "OPERATIONAL",
        "region": "us-east-1",
        "avatar": "img/avatar.svg",
        "tagline": "I build low-level systems, and I care most about the parts "
                   "that have to keep running.",
        "stack": ["OCaml", "Rust", "Go", "TypeScript", "Python", "C", "Linux"],
        "links": {
            "site": "https://yinkavaughan.me",
            "github": "https://github.com/Builder106",
            "email": "mailto:vaughanolayinka@gmail.com",
        },
        "about": [],
        "experience": [],
        "education": [],
        "hobbies": [],
        "places": [],
    },

    # TODO(teammates): add yourself below — copy MEMBER_TEMPLATE, fill it in,
    # and drop a square photo at app/static/img/<your-handle>.jpg.
]


def member_by_handle(handle):
    """Return the member dict for a handle, or None."""
    return next((m for m in MEMBERS if m["handle"] == handle), None)


def all_hobbies():
    """Every member's hobbies, flattened and tagged with their owner — for the
    fleet-wide hobbies page."""
    return [
        {**h, "owner": m["name"], "owner_handle": m["handle"]}
        for m in MEMBERS
        for h in m.get("hobbies", [])
    ]


# --------------------------------------------------------------------------- #
# Copy this when adding yourself to MEMBERS. Lists can start empty ([]).
# --------------------------------------------------------------------------- #
MEMBER_TEMPLATE = {
    "handle": "first-last",            # lowercase, dashes — becomes your URL + tab
    "name": "First Last",
    "github": "your-gh-username",
    "role": "Production Engineering Fellow",
    "status": "OPERATIONAL",
    "region": "us-east-1",
    "avatar": "img/first-last.jpg",    # drop a square photo here
    "tagline": "One line on what you build.",
    "stack": ["Python", "..."],
    "links": {"github": "https://github.com/your-gh-username"},
    "about": ["A short paragraph or two about you."],
    "experience": [
        {"ts": "2026-06", "service": "Where / what", "role": "Your role",
         "summary": "What you did.", "stack": ["..."], "metric": "", "url": ""},
    ],
    "education": [
        {"institution": "Your School", "credential": "Degree — Major",
         "location": "City", "term": "Class of 20XX", "detail": ""},
    ],
    "hobbies": [
        {"title": "Hobby", "summary": "One line.", "image": "img/your-hobby.jpg"},
    ],
    "places": [
        {"city": "City", "country": "Country", "lat": 0.0, "lng": 0.0,
         "kind": "home", "note": ""},
    ],
}
