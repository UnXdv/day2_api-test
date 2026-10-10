import requests

BASE = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    r = requests.get(f"{BASE}/posts", timeout= 10)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) == 100

def test_get_post_by_id():
    r = requests.get(f"{BASE}/posts/1", timeout= 10)
    assert r.status_code == 200
    assert r.json()["id"] == 1

def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    r = requests.post(f"{BASE}/posts",  data=payload, timeout= 10)
    assert r.status_code == 201
    assert r.json()["title"] == "foo"

def test_update_post():
    payload = {"id": 1, "title": "new", "body": "x", "userId": 1}
    r = requests.put(f"{BASE}/posts/1", json=payload, timeout= 10)
    assert r.status_code == 200
    assert r.json()["title"] == "new"

def test_patch_post():
    r = requests.patch(f"{BASE}/posts/1",
                       json={"title": "patched"}, timeout= 10)
    assert r.status_code == 200
    assert r.json()["title"] == "patched"

def test_delete_post():
    r = requests.delete(f"{BASE}/posts/1", timeout= 10)
    assert r.status_code == 200

def test_filter_by_user():
    r = requests.get(f"{BASE}/posts", params={"userId": 1},
                     
                      timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert len(data) > 0
    assert all(p["userId"] == 1 for p in data)

def test_get_comments():
    r = requests.get(f"{BASE}/posts/1/comments", timeout= 10)
    assert r.status_code == 200
    assert isinstance(r.json(),list)

def test_post_not_found():
    r = requests.get(f"{BASE}/posts/99999", timeout= 10)
    assert r.status_code == 404

def test_get_posts_with_client(json_api):
    r = json_api.get("/posts")
    assert r.status_code == 200
    assert len(r.json()) == 100

def test_create_post_with_client(json_api):
    r = json_api.post("/posts", json = {"title": "t", "body": "b", "userId": "1"})
    assert r.status_code == 201