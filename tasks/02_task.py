"""Task 2: Save the Apaleo response to a JSON file.

fetch_reservations() below is the solution to Task 1 - you can use it as-is.
Your new job is to save that data to a file, exactly as it came back from the
API (no picking and choosing fields yet - that's Task 3).

Run it with:
    make run FILE=tasks/02_task.py

Afterwards, check that the file was created and open it to look at its
contents:
    data/raw/reservations.json

TODO:
1. Make sure the "data/raw" folder exists (os.makedirs(..., exist_ok=True)).
2. Open JSON_PATH for writing, with encoding="utf-8".
3. Use json.dump(data, file, indent=2, ensure_ascii=False) to write it.
"""

from __future__ import annotations

import json
import os

from integrations.apaleo import ApaleoClient

PROPERTY_ID = "BER"
DATE_FROM = "2026-07-01T00:00:00Z"
DATE_TO = "2026-07-07T23:59:59Z"

JSON_PATH = "data/raw/reservations.json"


def fetch_reservations() -> dict:
    """Call the Apaleo reservations endpoint and return the parsed JSON. (Task 1 solution.)"""

    client = ApaleoClient(scope="reservations.read")
    response = client.get(
        "/booking/v1/reservations",
        params={
            "propertyIds": [PROPERTY_ID],
            "dateFilter": "Stay",
            "from": DATE_FROM,
            "to": DATE_TO,
        },
    )
    return response.json()


def save_json(data: dict) -> None:
    """Save the full API response to JSON_PATH, unchanged."""

    # TODO: create the "data/raw" folder if it doesn't exist yet, then write `data` to JSON_PATH.
    raise NotImplementedError("Task 2: save `data` to JSON_PATH.")


def main() -> None:
    data = fetch_reservations()
    save_json(data)
    print(f"Saved full response to {JSON_PATH}")


if __name__ == "__main__":
    main()
