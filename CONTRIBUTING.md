# Contributing

This is a personal portfolio for the MLH × Meta Production Engineering
fellowship — not a team repo. The site is an ops console for one service:
status header, `whoami`, `deploy.log`, build provenance, edge network.

The notes below are dev setup and guardrails for working on this repo. If
you're a fellow who wants to reuse the ops-console template for your own
portfolio, fork it and start by rewriting `PROFILE` in `app/data.py`.

## Dev setup

```bash
git clone https://github.com/Builder106/MLH-Meta-PE-Portfolio.git
cd MLH-Meta-PE-Portfolio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask run
```

Open <http://127.0.0.1:5000>. (`FLASK_APP`/debug come from `.flaskenv`; needs
Python 3.12+.)

## How the site is wired

- **All content is data.** `app/data.py` holds a single `PROFILE` dict.
  Routes in `app/__init__.py` render it through Jinja; templates have no
  hard-coded content.
- **Reusable macros** (`app/templates/macros.html`: `experience_item`,
  `education_item`, `hobby_card`) render repeating sections; pages just loop.

## Workflow

Solo repo, but still branch + PR per change so CI gates every merge and
`JOURNAL.md` has a natural place to log the change:

1. **Branch** off `main`: `feat/<short-name>` (or `fix/`, `docs/`, `chore/`).
2. Commit, push, open a PR.
3. Merge once CI is green.

Keep PRs small and focused — one feature/fix per PR.

## Guardrails

- **Content goes in `app/data.py`, not in templates.** If you're editing a
  `.html` file to change words, it probably belongs in `data.py`.
- **Keep the ops-console aesthetic** — white canvas, Inter, the one deep-blue
  accent (see `app/static/styles/main.css` for the actual tokens). New
  colours/fonts should be a deliberate, discussed change, not a one-off.
- **Don't commit secrets.** `.env` is gitignored; use it for anything sensitive.
- Run the app locally before opening a PR — `/` should load without errors.
