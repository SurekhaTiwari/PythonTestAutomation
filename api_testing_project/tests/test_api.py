"""
Simple API Testing project (Module 11) using Python + requests + pytest.

Public APIs used:
  - JSONPlaceholder : https://jsonplaceholder.typicode.com  (CRUD / REST)
  - httpbin         : https://httpbin.org                   (headers, auth, XML, status codes)
"""
import xml.etree.ElementTree as ET

import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
HTTPBIN = "https://httpbin.org"
TIMEOUT = 10


@pytest.fixture(scope="session")
def api():
    """One reusable HTTP session with default headers (HTTPS, headers)."""
    session = requests.Session()
    session.headers.update({
        "Accept": "application/json",
        "User-Agent": "api-testing-demo/1.0",
    })
    return session


# ---------------------------------------------------------------
# 1. GET - request/response, status code, headers, JSON
# ---------------------------------------------------------------
def test_get_single_post(api):
    response = api.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    body = response.json()
    assert body["id"] == 1
    assert {"userId", "id", "title", "body"} <= body.keys()


def test_get_list_of_posts(api):
    response = api.get(f"{BASE_URL}/posts", timeout=TIMEOUT)

    assert response.status_code == 200
    assert len(response.json()) == 100


# ---------------------------------------------------------------
# 2. Query parameters
# ---------------------------------------------------------------
def test_get_with_query_parameters(api):
    response = api.get(f"{BASE_URL}/posts", params={"userId": 1}, timeout=TIMEOUT)

    assert response.status_code == 200
    posts = response.json()
    assert len(posts) > 0
    assert all(post["userId"] == 1 for post in posts)


# ---------------------------------------------------------------
# 3. POST - create (201 Created)
# ---------------------------------------------------------------
def test_post_create_resource(api):
    payload = {"title": "QA post", "body": "Learning API testing", "userId": 1}
    response = api.post(f"{BASE_URL}/posts", json=payload, timeout=TIMEOUT)

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == payload["title"]
    assert "id" in body


# ---------------------------------------------------------------
# 4. PUT - full update
# ---------------------------------------------------------------
def test_put_update_resource(api):
    payload = {"id": 1, "title": "Updated", "body": "Updated body", "userId": 1}
    response = api.put(f"{BASE_URL}/posts/1", json=payload, timeout=TIMEOUT)

    assert response.status_code == 200
    assert response.json()["title"] == "Updated"


# ---------------------------------------------------------------
# 5. PATCH - partial update
# ---------------------------------------------------------------
def test_patch_partial_update(api):
    response = api.patch(f"{BASE_URL}/posts/1", json={"title": "Patched"}, timeout=TIMEOUT)

    assert response.status_code == 200
    assert response.json()["title"] == "Patched"


# ---------------------------------------------------------------
# 6. DELETE
# ---------------------------------------------------------------
def test_delete_resource(api):
    response = api.delete(f"{BASE_URL}/posts/1", timeout=TIMEOUT)

    assert response.status_code == 200


# ---------------------------------------------------------------
# 7. Negative testing - invalid resource -> 404
# ---------------------------------------------------------------
def test_get_non_existing_resource_returns_404(api):
    response = api.get(f"{BASE_URL}/posts/99999", timeout=TIMEOUT)

    assert response.status_code == 404


# ---------------------------------------------------------------
# 8. Status codes (parameterized)
# ---------------------------------------------------------------
@pytest.mark.parametrize("code", [200, 201, 400, 401, 404, 500])
def test_various_status_codes(api, code):
    response = api.get(f"{HTTPBIN}/status/{code}", timeout=TIMEOUT)

    assert response.status_code == code


# ---------------------------------------------------------------
# 9. Custom request headers
# ---------------------------------------------------------------
def test_custom_request_header(api):
    response = api.get(
        f"{HTTPBIN}/headers", headers={"X-Course": "API-Testing"}, timeout=TIMEOUT
    )

    assert response.status_code == 200
    assert response.json()["headers"]["X-Course"] == "API-Testing"


# ---------------------------------------------------------------
# 10. Authentication - Basic Auth (positive + negative)
# ---------------------------------------------------------------
def test_basic_auth_valid_credentials(api):
    response = api.get(f"{HTTPBIN}/basic-auth/user/pass", auth=("user", "pass"), timeout=TIMEOUT)

    assert response.status_code == 200
    assert response.json()["authenticated"] is True


def test_basic_auth_invalid_credentials(api):
    response = api.get(f"{HTTPBIN}/basic-auth/user/pass", auth=("user", "wrong"), timeout=TIMEOUT)

    assert response.status_code == 401


# ---------------------------------------------------------------
# 11. Authorization - Bearer token (positive + negative)
# ---------------------------------------------------------------
def test_bearer_token_valid(api):
    response = api.get(
        f"{HTTPBIN}/bearer", headers={"Authorization": "Bearer my-token"}, timeout=TIMEOUT
    )

    assert response.status_code == 200
    assert response.json()["token"] == "my-token"


def test_bearer_token_missing(api):
    response = api.get(f"{HTTPBIN}/bearer", timeout=TIMEOUT)

    assert response.status_code == 401


# ---------------------------------------------------------------
# 12. XML response processing
# ---------------------------------------------------------------
def test_xml_response(api):
    response = api.get(f"{HTTPBIN}/xml", headers={"Accept": "application/xml"}, timeout=TIMEOUT)

    assert response.status_code == 200
    assert "xml" in response.headers["Content-Type"]

    root = ET.fromstring(response.text)
    assert root.tag == "slideshow"
    assert root.attrib["title"] == "Sample Slide Show"
