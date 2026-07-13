"""Placeholder backend API for the reservation dashboard (index.html).

Run with: flask --app api run --host 0.0.0.0 --port 5000
"""

from __future__ import annotations

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/api/playground")
def get_playground():
    return jsonify({})


@app.get("/api/reservations")
def get_reservations():
    return jsonify({})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
