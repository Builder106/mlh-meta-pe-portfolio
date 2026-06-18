"""Flask app for the pod portfolio.

The site is an ops console for a *fleet*: the pod is a cluster, each teammate is
a service. ``/`` lists the fleet, ``/u/<handle>`` is a service's detail page, and
``/ps_aux`` is the fleet-wide background-process (hobbies) view. All content comes
from ``app.data`` so templates stay logic-light, and the menu bar is generated
from ``MEMBERS`` — add a member and a tab + a page appear automatically.
"""
import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, jsonify, abort

from . import data

load_dotenv()

app = Flask(__name__)


@app.context_processor
def inject_globals():
    """Build the dynamic nav (fleet + a tab per member + ps_aux) and expose the
    pod to every template. Active tab is resolved from the current endpoint."""
    nav = [{"label": "Team", "url": url_for("fleet"),
            "active": request.endpoint == "fleet"}]
    for m in data.MEMBERS:
        nav.append({
            "label": m["name"].split()[0],
            "url": url_for("member", handle=m["handle"]),
            "active": (request.endpoint == "member"
                       and request.view_args.get("handle") == m["handle"]),
        })
    nav.append({"label": "Hobbies", "url": url_for("hobbies"),
                "active": request.endpoint == "hobbies"})
    return {
        "nav": nav,
        "pod": data.POD,
        "now": datetime.now(timezone.utc),
        "site_url": os.getenv("URL", "localhost:5000"),
    }


@app.route("/")
def fleet():
    return render_template("fleet.html", title=f"{data.POD['name']} — team",
                           members=data.MEMBERS)


@app.route("/u/<handle>")
def member(handle):
    m = data.member_by_handle(handle)
    if m is None:
        abort(404)
    return render_template("member.html",
                           title=f"{m['name']} — {data.POD['name']}", member=m)


@app.route("/ps_aux")
def hobbies():
    return render_template("hobbies.html", title=f"Hobbies — {data.POD['name']}",
                           procs=data.all_hobbies())


@app.route("/healthz")
def healthz():
    """Liveness probe — because of course a fleet has one."""
    return jsonify(
        pod=data.POD["name"],
        status=data.POD["status"],
        region=data.POD["region"],
        cohort=data.POD["cohort"],
        services=[m["handle"] for m in data.MEMBERS],
        checks={"members": len(data.MEMBERS),
                "processes": len(data.all_hobbies())},
        ts=datetime.now(timezone.utc).isoformat(),
    )


@app.errorhandler(404)
def not_found(_e):
    return render_template("404.html", title="404 — no such service"), 404
