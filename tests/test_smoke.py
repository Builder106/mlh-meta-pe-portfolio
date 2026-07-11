"""Smoke tests — boot the app and assert every route serves.

These run in CI on every PR. A malformed PROFILE field 500s the page and
fails CI before merge.
"""
import app as application


def client():
    return application.app.test_client()


def test_core_routes_ok():
    c = client()
    for path in ("/", "/ps_aux", "/healthz", "/timeline"):
        assert c.get(path).status_code == 200, path


def test_unknown_route_404():
    assert client().get("/does-not-exist").status_code == 404


def test_healthz_counts_hobbies():
    payload = client().get("/healthz").get_json()
    assert payload["checks"]["processes"] == len(application.data.PROFILE["hobbies"])


def test_timeline_post_create_and_list():
    c = client()
    created = c.post("/api/timeline_post", json={
        "name": "CI Runner", "email": "ci@example.com", "content": "smoke test post",
    })
    assert created.status_code == 201, created.get_data(as_text=True)
    post_id = created.get_json()["id"]

    listed = c.get("/api/timeline_post").get_json()
    assert any(p["id"] == post_id for p in listed)

    assert c.delete(f"/api/timeline_post/{post_id}").status_code == 200


def test_timeline_post_requires_fields():
    resp = client().post("/api/timeline_post", json={"name": "Missing Fields"})
    assert resp.status_code == 400
