"""Fetch reservations from the apaleo Booking API.

Usage:
    python fetch_apaleo_reservations.py \
        --property-id <PROPERTY_ID> \
        --from 2026-07-01T00:00:00Z \
        --to 2026-07-31T23:59:59Z

The script reads APALEO_CLIENT_ID and APALEO_CLIENT_SECRET from the
environment, typically via a local .env file.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from typing import Any

from integrations.apaleo import ApaleoClient


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch Apaleo reservations for one property and date range."
    )
    parser.add_argument(
        "--property-id",
        required=True,
        help="Apaleo property id to filter reservations for.",
    )
    parser.add_argument(
        "--from",
        dest="date_from",
        required=True,
        help="Start of the interval in ISO-8601 format, e.g. 2026-07-01T00:00:00Z.",
    )
    parser.add_argument(
        "--to",
        dest="date_to",
        required=True,
        help="End of the interval in ISO-8601 format, e.g. 2026-07-31T23:59:59Z.",
    )
    parser.add_argument(
        "--date-filter",
        default="Stay",
        choices=[
            "Arrival",
            "Departure",
            "Stay",
            "Creation",
            "Modification",
            "Cancellation",
            "ArrivalAndCheckIn",
            "DepartureAndCheckOut",
        ],
        help="Reservation date field to filter by. Default: Stay.",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=500,
        help="Items per page. Default: 500.",
    )
    parser.add_argument(
        "--page-number",
        type=int,
        default=1,
        help="Page number to retrieve. Default: 1.",
    )
    return parser.parse_args()


def parse_iso_datetime(value: str) -> str:
    normalized_value = value.strip()
    if normalized_value.endswith("Z"):
        normalized_value = normalized_value[:-1] + "+00:00"

    parsed_value = datetime.fromisoformat(normalized_value)
    if parsed_value.tzinfo is None:
        parsed_value = parsed_value.replace(tzinfo=timezone.utc)

    return parsed_value.isoformat().replace("+00:00", "Z")


def build_query_params(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "propertyIds": [args.property_id],
        "dateFilter": args.date_filter,
        "from": parse_iso_datetime(args.date_from),
        "to": parse_iso_datetime(args.date_to),
        "pageSize": args.page_size,
        "pageNumber": args.page_number,
    }


def main() -> int:
    args = parse_args()
    client = ApaleoClient(scope="reservations.read")

    response = client.get("/booking/v1/reservations", params=build_query_params(args))

    if not response.content:
        print(
            f"Received empty response body (HTTP {response.status_code}, "
            f"content-type={response.headers.get('Content-Type')})."
        )
        return 0

    try:
        payload = response.json()
    except ValueError as exc:
        raise SystemExit(
            f"Could not parse response as JSON (HTTP {response.status_code}, "
            f"content-type={response.headers.get('Content-Type')}): "
            f"{response.text[:500]!r}"
        ) from exc

    if isinstance(payload, dict):
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(json.dumps({"reservations": payload}, indent=2, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
