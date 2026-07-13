"""Task 3: Turn the saved JSON into a CSV file with only the fields we need.

This reads back the file written in Task 2 (data/raw/reservations.json) and
writes a smaller CSV file containing only the columns the database actually
needs: reservation_id, property_id, arrival, departure, adults, children,
status.

Run it with:
    make run FILE=tasks/03_task.py

(Run Task 2 first if data/raw/reservations.json doesn't exist yet.)

Note: the exact field names inside each reservation depend on the real
Apaleo response. If a key below doesn't exist in your data (e.g. "id" is
called something else), open data/raw/reservations.json and check with your
mentor - this is expected, it's part of "reviewing what's in the data".

TODO:
1. Load JSON_PATH with json.load().
2. Get the list of reservations from it (see get_reservation_list below).
3. For each reservation, build a row dict with exactly these keys:
   reservation_id, property_id, arrival, departure, adults, children, status
   (map them from the reservation's "id", "propertyId", "arrival",
   "departure", "adults", "children", "status" fields).
4. Write the rows to CSV_PATH using csv.DictWriter, with a header row.
"""

from __future__ import annotations

import csv
import json
import os

JSON_PATH = "data/raw/reservations.json"
CSV_PATH = "data/processed/reservations.csv"
CSV_FIELDS = ["reservation_id", "property_id", "arrival", "departure", "adults", "children", "status"]


def get_reservation_list(data: dict | list) -> list[dict]:
    """Apaleo may wrap the list under a "reservations" key, or return a plain list."""

    if isinstance(data, list):
        return data
    return data.get("reservations", [])


def load_json() -> dict | list:
    with open(JSON_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def build_rows(reservations: list[dict]) -> list[dict]:
    """Pick out only the fields we need from each reservation."""

    # TODO: build and return a list of row dicts, one per reservation, using CSV_FIELDS as keys.
    raise NotImplementedError("Task 3: build the list of row dicts.")


def save_csv(rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)

    with open(CSV_PATH, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    data = load_json()
    reservations = get_reservation_list(data)
    rows = build_rows(reservations)
    save_csv(rows)
    print(f"Saved {len(rows)} rows to {CSV_PATH}")


if __name__ == "__main__":
    main()
