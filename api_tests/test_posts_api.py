"""HTTP API tests using requests and a JSON payload.

Run with: python -m pytest api_tests -v
The default fixture is a local demo API, so tests run without internet access.
"""
import requests

TIMEOUT_SECONDS = 5


class TestPostsAPI:
    def test_get_post_returns_expected_fields(self, api_base_url):
        response = requests.get(f"{api_base_url}/posts/1", timeout=TIMEOUT_SECONDS)

        assert response.status_code == 200, response.text
        post = response.json()
        assert post["id"] == 1
        assert post["userId"] == 1
        assert isinstance(post["title"], str) and post["title"]
        assert isinstance(post["body"], str) and post["body"]

    def test_create_post_with_json_payload(self, api_base_url):
        # This JSON payload is sent in the HTTP POST request body.
        payload = {
            "title": "Playwright API test",
            "body": "Created by the Python automation framework.",
            "userId": 1,
        }

        response = requests.post(
            f"{api_base_url}/posts",
            json=payload,
            headers={"Content-Type": "application/json; charset=UTF-8"},
            timeout=TIMEOUT_SECONDS,
        )

        assert response.status_code == 201, response.text
        created_post = response.json()
        assert created_post["title"] == payload["title"]
        assert created_post["body"] == payload["body"]
        assert created_post["userId"] == payload["userId"]
        assert created_post["id"] == 101
