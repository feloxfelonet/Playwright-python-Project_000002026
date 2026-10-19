"""Local demo API fixture so API tests can run without internet access."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

import pytest


class DemoAPIHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/posts/1":
            self._send_json(200, {
                "userId": 1,
                "id": 1,
                "title": "sample post",
                "body": "sample post body",
            })
        else:
            self._send_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/posts":
            self._send_json(404, {"error": "not found"})
            return
        length = int(self.headers.get("Content-Length", "0"))
        payload = json.loads(self.rfile.read(length).decode("utf-8"))
        if not all(key in payload for key in ("title", "body", "userId")):
            self._send_json(400, {"error": "title, body and userId are required"})
            return
        self._send_json(201, {**payload, "id": 101})

    def log_message(self, format, *args):
        # Keep test output concise.
        return


@pytest.fixture(scope="session")
def api_base_url():
    server = ThreadingHTTPServer(("127.0.0.1", 0), DemoAPIHandler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    host, port = server.server_address
    yield f"http://{host}:{port}"
    server.shutdown()
    server.server_close()
    thread.join(timeout=2)
