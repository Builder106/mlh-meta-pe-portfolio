"""Single source of truth for the portfolio's content.

This is a *pod* portfolio: a fleet of services, one per teammate. The landing
page lists every member as a service; each member gets their own detail page at
``/u/<handle>`` automatically, and the menu bar grows a tab per member. Add a
dict to ``MEMBERS`` (and drop an avatar) and you appear everywhere — no template
or route changes needed.

ADDING YOURSELF (teammates start here):
  1. Copy the MEMBER_TEMPLATE block at the bottom into MEMBERS.
  2. Fill in your real details. `handle` becomes your URL + nav tab.
  3. Drop a square photo at app/static/photos/<your-handle>.jpg.
  4. `flask run` → you're on the fleet overview and have your own page.
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
        "avatar": "photos/olayinka-vaughan.jpg",
        "tagline": "I build low-level systems, and I care most about the parts "
                   "that have to keep running.",
        "stack": ["OCaml", "Rust", "Go", "TypeScript", "Python", "C", "Linux"],
        "links": {
            "site": "https://yinkavaughan.me",
            "github": "https://github.com/Builder106",
            "email": "mailto:vaughanolayinka@gmail.com",
        },

        # whoami / about — one string per paragraph.
        "about": [
            "I'm a student at Wesleyan, and this summer I'm a Production "
            "Engineering Fellow with MLH and Meta.",

            "Most of what I build sits low in the stack. The project I've sunk "
            "the most hours into is a limit order book in OCaml that I got down "
            "to zero allocations on the matching path. There's also a Rust tool "
            "that rebuilds packages and checks them byte for byte, and a small "
            "Go proxy that sits between an LLM and its tools to screen what it's "
            "allowed to call. Lately I've been benchmarking the same workloads "
            "across a few Linux distros on identical VMs, just to see what "
            "actually differs.",

            "The thread through all of it is that I'd rather measure something "
            "than take it on faith. That's most of why production engineering "
            "appealed to me.",
        ],

        # deploy.log — env: fellowship | oss | research | work
        #              status: running | stable | shipped
        "experience": [
            {
                "ts": "2026-06", "env": "fellowship", "status": "running",
                "service": "MLH × Meta — Production Engineering Fellowship",
                "role": "Production Engineering Fellow · cohort 26.SUM.B",
                "summary": "A 12-week fellowship mentored by Meta engineers, "
                           "focused on the operational side of running software "
                           "in production.",
                "stack": ["Linux", "Flask", "Git", "Docker"],
                "url": "https://fellowship.mlh.io/programs/production-engineering",
            },
            {
                "ts": "2026-06", "env": "research", "status": "shipped",
                "service": "Enclave",
                "role": "Local-first clinical-document pipeline",
                "summary": "Agentic extraction + ICD-10/CPT matching with PHI "
                           "egress (bytes off-machine) tracked as a first-class "
                           "metric, measured across a rules floor, an on-device "
                           "3B, and hosted baselines.",
                "stack": ["TypeScript", "On-device LLM", "FHIR"],
                "metric": "PHI egress = 0 B on-device path",
                "url": "https://enclave-iota.vercel.app",
            },
            {
                "ts": "2026-05", "env": "oss", "status": "stable",
                "service": "ClearHash",
                "role": "Rust supply-chain integrity verifier",
                "summary": "Rebuild every package, compare every byte, block "
                           "every tamper. Reproducible-build verification driven "
                           "by Sigstore + SLSA.",
                "stack": ["Rust", "Sigstore", "SLSA"],
                "metric": "byte-for-byte rebuild diffing",
                "url": "https://clearhash.vercel.app",
            },
            {
                "ts": "2026-05", "env": "oss", "status": "stable",
                "service": "Halberd",
                "role": "JSON-RPC firewall for MCP agents",
                "summary": "Inspects every tools/call between an LLM and its MCP "
                           "servers, blocking argument injection and capability "
                           "creep before they reach the host.",
                "stack": ["Go", "MCP", "JSON-RPC"],
                "metric": "inline call inspection",
                "url": "https://halberd-keep.vercel.app",
            },
            {
                "ts": "2026-05", "env": "oss", "status": "stable",
                "service": "Quarry",
                "role": "Bare-metal MEV arbitrage bot",
                "summary": "TypeScript mempool scanner + Yul executor + Aave V3 "
                           "flashloans. Built for the smallest possible runtime "
                           "and gas footprint.",
                "stack": ["TypeScript", "Yul", "EVM"],
                "metric": "188 B runtime · 110k gas/2-hop · 99.89% acc.",
                "url": "https://quarry-mev.vercel.app",
            },
            {
                "ts": "2026-04", "env": "oss", "status": "stable",
                "service": "ocaml_limit",
                "role": "Zero-allocation Limit Order Book engine",
                "summary": "High-performance LOB matching engine in OCaml 5 with "
                           "a real-time, high-density dashboard inspired by the "
                           "Bloomberg Terminal.",
                "stack": ["OCaml 5", "Domains", "Vite"],
                "metric": "0 allocations per submit",
                "url": "https://ocaml-lob.vercel.app",
            },
            {
                "ts": "2026-03", "env": "research", "status": "shipped",
                "service": "CapitolAlpha",
                "role": "Wesleyan QAC 420 — quantitative finance",
                "summary": "Pipelined 16,203 disclosed Congressional stock trades "
                           "(2020–2024) and measured a +2.58% Jensen's alpha vs "
                           "the S&P 500, significant at p < 0.05.",
                "stack": ["Python", "pandas", "statsmodels"],
                "metric": "+2.58% α · p < 0.05 · n = 16,203",
                "url": "https://capitolalpha.vercel.app",
            },
            {
                "ts": "2024-10", "env": "oss", "status": "stable",
                "service": "LinuxBenchHub",
                "role": "VM benchmarking platform",
                "summary": "Runs the Phoronix Test Suite across Ubuntu, Fedora, "
                           "and Debian under identical virtual hardware, with a "
                           "Rails 8 dashboard and an embedded noVNC live view.",
                "stack": ["Rails 8", "Phoronix", "noVNC", "KVM"],
                "metric": "identical-hardware cross-distro runs",
                "url": "https://linuxbenchhub.vercel.app",
            },
            # TODO(you): add internships / employment here.
        ],

        # build provenance — education.
        "education": [
            {
                "institution": "Wesleyan University",
                "credential": "B.A. — Computer Science & Economics (double major)",
                "location": "Middletown, CT",
                "term": "Class of 2028",
                "detail": "Coursework through the Quantitative Analysis Center "
                          "(QAC): built CapitolAlpha for QAC 420 and ran the "
                          "DuckDB pipeline for DataFest 2026.",
            },
            {
                "institution": "Dominican University of California",
                "credential": "ACS-4996 — Supervised Work Experience "
                              "(MLH × Meta Fellowship)",
                "location": "Remote · Summer 2026",
                "term": "2026",
                "detail": "Concurrent enrollment carrying the MLH Production "
                          "Engineering Fellowship as for-credit work experience "
                          "(10 units).",
            },
        ],

        # hobbies (with images).
        "hobbies": [
            {
                "title": "Piano",
                "summary": "I've played piano for years, including at my church.",
                "image": "photos/hobby-piano.jpg",
            },
            {
                "title": "Basketball",
                "summary": "Pickup basketball at the local courts — my main way "
                           "to get off the screen and outside.",
                "image": "photos/hobby-basketball.jpg",
            },
        ],

        # places travelled (map). kind: home | origin | visited
        "places": [
            {"city": "Middletown", "country": "USA", "lat": 41.5623,
             "lng": -72.6506, "kind": "home", "note": "Wesleyan — where I study"},
            {"city": "Lagos", "country": "Nigeria", "lat": 6.5244,
             "lng": 3.3792, "kind": "origin", "note": "where I'm from"},
            # TODO(you): add every city you've actually travelled to.
        ],
    },

    # TODO(teammates): add yourself below. Copy MEMBER_TEMPLATE, fill it in, and
    # drop a square photo at app/static/photos/<your-handle>.jpg.
]


def member_by_handle(handle):
    """Return the member dict for a handle, or None."""
    return next((m for m in MEMBERS if m["handle"] == handle), None)


def all_hobbies():
    """Every member's hobbies, flattened and tagged with their owner — for the
    fleet-wide `ps aux` page."""
    return [
        {**h, "owner": m["name"], "owner_handle": m["handle"]}
        for m in MEMBERS
        for h in m.get("hobbies", [])
    ]


# --------------------------------------------------------------------------- #
# Copy this when adding yourself to MEMBERS. Delete the fields you don't use;
# `hobbies`, `education`, and `places` can start empty ([]).
# --------------------------------------------------------------------------- #
MEMBER_TEMPLATE = {
    "handle": "first-last",            # lowercase, dashes — becomes your URL + tab
    "name": "First Last",
    "github": "your-gh-username",
    "role": "Production Engineering Fellow",
    "status": "OPERATIONAL",
    "region": "us-east-1",             # pick anything; it's flavor
    "avatar": "photos/first-last.jpg",    # drop a square photo here
    "tagline": "One line on what you build.",
    "stack": ["Python", "..."],
    "links": {"github": "https://github.com/your-gh-username"},
    "about": ["A short paragraph or two about you."],
    "experience": [
        {"ts": "2026-06", "env": "work", "status": "stable",
         "service": "Where / what", "role": "Your role",
         "summary": "What you did.", "stack": ["..."], "metric": "", "url": ""},
    ],
    "education": [
        {"institution": "Your School", "credential": "Degree — Major",
         "location": "City", "term": "Class of 20XX", "detail": ""},
    ],
    "hobbies": [
        {"title": "Hobby", "summary": "One line.", "image": "photos/your-hobby.jpg"},
    ],
    "places": [
        {"city": "City", "country": "Country", "lat": 0.0, "lng": 0.0,
         "kind": "home", "note": ""},
    ],
}
