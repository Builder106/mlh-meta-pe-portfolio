"""Single source of truth for the portfolio's content.

This is an individual portfolio for one MLH × Meta Production Engineering
fellow, not a shared team site. Everything the templates render lives in
``PROFILE`` below, so content edits never need a template change.
"""

# --------------------------------------------------------------------------- #
# Profile — the one person this site describes.
# --------------------------------------------------------------------------- #
PROFILE = {
    "name": "Olayinka Vaughan",
    "handle": "olayinka-vaughan",
    "github": "Builder106",
    "role": "Production Engineering Fellow",
    "label": "MLH × Meta — Production Engineering Fellow",
    "cohort": "26.SUM.B.6",
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
    "repo": "https://github.com/Builder106/MLH-Meta-PE-Portfolio",

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
}
