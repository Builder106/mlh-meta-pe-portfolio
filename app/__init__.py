"""Flask app for an individual portfolio.

The site is an ops console for one person: ``/`` is the profile — status
header, ``whoami``, ``deploy.log``, build provenance, edge network — and
``/ps_aux`` is the background-process (hobbies) view. All content comes from
``app.data.PROFILE`` so templates stay logic-light.
"""
import hashlib
import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, jsonify

from peewee import CharField, DateTimeField, Model, MySQLDatabase, TextField
from playhouse.shortcuts import model_to_dict

from . import data

load_dotenv()

app = Flask(__name__)

db = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    host=os.getenv("MYSQL_HOST", "localhost"),
    port=int(os.getenv("MYSQL_PORT", 3306)),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
)


class TimelinePost(Model):
    """A post on the public timeline — school + career updates."""

    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    class Meta:
        database = db


db.connect()
db.create_tables([TimelinePost])
db.close()


@app.before_request
def _db_connect():
    db.connect(reuse_if_open=True)


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()


def gravatar_url(email, size=64):
    """Gravatar's hash-of-email avatar convention; `d=identicon` covers posters
    without a registered Gravatar."""
    digest = hashlib.md5(email.strip().lower().encode("utf-8")).hexdigest()
    return f"https://www.gravatar.com/avatar/{digest}?s={size}&d=identicon"


app.jinja_env.globals["gravatar_url"] = gravatar_url


def serialize_post(post):
    payload = model_to_dict(post)
    payload["gravatar"] = gravatar_url(post.email)
    return payload


@app.context_processor
def inject_globals():
    """Expose the profile and a fixed nav to every template."""
    nav = [
        {"label": "Home", "url": url_for("home"), "active": request.endpoint == "home"},
        {"label": "Hobbies", "url": url_for("hobbies"), "active": request.endpoint == "hobbies"},
        {"label": "Timeline", "url": url_for("timeline"), "active": request.endpoint == "timeline"},
    ]
    return {
        "nav": nav,
        "profile": data.PROFILE,
        "now": datetime.now(timezone.utc),
        "site_url": os.getenv("URL", "localhost:5000"),
    }


@app.route("/")
def home():
    return render_template("home.html", title=f"{data.PROFILE['name']} — {data.PROFILE['role']}",
                           profile=data.PROFILE)


@app.route("/ps_aux")
def hobbies():
    return render_template("hobbies.html", title=f"Hobbies — {data.PROFILE['name']}",
                           procs=data.PROFILE["hobbies"])


@app.route("/timeline")
def timeline():
    posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return render_template("timeline.html",
                           title=f"Timeline — {data.PROFILE['name']}", posts=posts)


@app.route("/api/timeline_post", methods=["POST"])
def create_timeline_post():
    payload = request.get_json(silent=True) or request.form
    name = (payload.get("name") or "").strip()
    email = (payload.get("email") or "").strip()
    content = (payload.get("content") or "").strip()
    if not name or not email or not content:
        return jsonify(error="name, email, and content are all required"), 400
    post = TimelinePost.create(name=name, email=email, content=content)
    return jsonify(serialize_post(post)), 201


@app.route("/api/timeline_post", methods=["GET"])
def list_timeline_posts():
    posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return jsonify([serialize_post(p) for p in posts])


@app.route("/api/timeline_post/<int:post_id>", methods=["DELETE"])
def delete_timeline_post(post_id):
    post = TimelinePost.get_or_none(TimelinePost.id == post_id)
    if post is None:
        return jsonify(error="not found"), 404
    post.delete_instance()
    return jsonify(deleted=post_id)


@app.route("/healthz")
def healthz():
    """Liveness probe — because of course a service has one."""
    return jsonify(
        service=data.PROFILE["handle"],
        status=data.PROFILE["status"],
        region=data.PROFILE["region"],
        cohort=data.PROFILE["cohort"],
        checks={"processes": len(data.PROFILE["hobbies"])},
        ts=datetime.now(timezone.utc).isoformat(),
    )


@app.errorhandler(404)
def not_found(_e):
    return render_template("404.html", title="404 — no such service"), 404
