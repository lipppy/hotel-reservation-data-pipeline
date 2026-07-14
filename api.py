"""Placeholder backend API for the reservation dashboard (index.html).

Run with: flask --app api run --host 0.0.0.0 --port 5000
"""

from __future__ import annotations

import json

from flask import Flask, jsonify

app = Flask(__name__)

DEMO_RESERVATIONS_PATH = "data/demo_reservations.json"


@app.get("/api/reservations-demo")
def get_reservations_demo():
    with open(DEMO_RESERVATIONS_PATH, "r", encoding="utf-8") as file:
        return jsonify(json.load(file))


@app.get("/api/reservations")
def get_reservations():
    return jsonify({})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
