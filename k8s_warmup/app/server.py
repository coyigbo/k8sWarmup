import os
import socket
from datetime import datetime, timezone
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.get("/")
def root():
    hostname = socket.gethostname()
    now = datetime.now(timezone.utc).isoformat()
    return (
        f"OK - k8s-warmup\n"
        f"path: {request.path}\n"
        f"hostname: {hostname}\n"
        f"timestamp: {now}\n"
    ), 200, {"Content-Type": "text/plain; charset=utf-8"}


def run() -> None:
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    run()


