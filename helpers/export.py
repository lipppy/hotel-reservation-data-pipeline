"""File-export helpers for reservation records.

Save whatever integrations.apaleo.get_reservations / integrations.db.get_reservations
already returned to disk, one file per (property_id, date_from, date_to) request -
the file name encodes those inputs so repeated calls with different
properties/date ranges don't overwrite each other.
"""

from __future__ import annotations

import csv
import json
import os

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

DEFAULT_CSV_FIELDS = [
    "reservation_id",
    "property_id",
    "arrival",
    "departure",
    "adults",
    "children",
    "status",
]


def _export_filename(
    property_id: str,
    date_from: str | None,
    date_to: str | None,
    extension: str,
) -> str:
    parts = [property_id, date_from or "all", date_to or "all"]
    return f"reservations_{'_'.join(parts)}.{extension}"


def dump_to_json(
    records: list[dict],
    property_id: str,
    date_from: str | None = None,
    date_to: str | None = None,
) -> str:
    """Save `records` as JSON under data/raw/. Returns the path written to."""

    os.makedirs(RAW_DIR, exist_ok=True)
    path = os.path.join(RAW_DIR, _export_filename(property_id, date_from, date_to, "json"))

    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False, default=str)

    return path


def dump_to_csv(
    records: list[dict],
    property_id: str,
    date_from: str | None = None,
    date_to: str | None = None,
) -> str:
    """Save `records` as CSV under data/processed/. Returns the path written to."""

    os.makedirs(PROCESSED_DIR, exist_ok=True)
    path = os.path.join(PROCESSED_DIR, _export_filename(property_id, date_from, date_to, "csv"))
    fieldnames = list(records[0].keys()) if records else DEFAULT_CSV_FIELDS

    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    return path
