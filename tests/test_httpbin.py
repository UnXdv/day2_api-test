import pytest
import requests

BASE = "https://httpbin.org"

def test_get_status():
    r = requests.get(f"{BASE}/get", timeout=10)
    assert r.status_code == 200

def test_get_params():
    r = requests.get(f"{BASE}/get", params={"a": 1, "b": "x"}, timeout=10)
    assert r.json()["args"] == {"a": "1", "b": "x"}

def test_post_json():
    payload = {"name": "tom", "age": 18}
    r = requests.post(f"{BASE}/post", json= payload, timeout= 10)
    assert r.status_code == 200
    assert r.json()["json"] == payload

def test_post_form():
    r = requests.post(f"{BASE}/post", data={"a": "1"}, timeout= 10)
    assert r.json()["form"] == {"a": "1"}

def test_headers():
    r = requests.get(f"{BASE}/headers",
                     headers={"token": "abc"}, timeout= 10)
    assert r.json()["headers"]["Token"] == "abc"

def test_basic_auth_success():
    r = requests.get(f"{BASE}/basic-auth/user/pass",
                     auth=("user", "pass"), timeout= 10)
    assert r.status_code == 200
    assert r.json()["authenticated"] is True

@pytest.mark.parametrize("code", [200, 201, 400, 404, 500])
def test_status_code(code):
    r = requests.get(f"{BASE}/status/{code}", timeout= 10)
    assert r.status_code == code

def test_delay():
    r = requests.get(f"{BASE}/delay/1", timeout= 5)
    assert r.status_code == 200

def test_not_found():
    r = requests.get(f"{BASE}/status/404", timeout= 10)
    assert r.status_code == 404

