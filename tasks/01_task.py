"""Task 1: Call the Apaleo reservations API.

The Apaleo client is already built for you (see integrations/apaleo/client.py).
Your job here is only to USE it: initialize it and call the reservations
endpoint for one hotel and one date range, then print what comes back so you
can see what a reservation actually looks like.

Run it with:
    make run FILE=tasks/01_task.py

TODO:
1. Create an ApaleoClient(scope="reservations.read").
2. Call client.get("/booking/v1/reservations", params=...) with:
   - propertyIds: [PROPERTY_ID]
   - dateFilter: "Stay"
   - from: DATE_FROM
   - to: DATE_TO
3. Turn the response into a Python object with response.json().
4. Print it with json.dumps(..., indent=2) so it's readable.
"""

from __future__ import annotations

import json

from integrations.apaleo import ApaleoClient

# Change these once you have real credentials and a real hotel code to test with.
PROPERTY_ID = "BER"
DATE_FROM = "2026-07-01T00:00:00Z"
DATE_TO = "2026-07-07T23:59:59Z"


def fetch_reservations() -> dict:
    """Call the Apaleo reservations endpoint and return the parsed JSON."""

    # TODO: create the client and call the endpoint, then return response.json()
    raise NotImplementedError("Task 1: call the Apaleo API and return the JSON result.")


def main() -> None:
    data = fetch_reservations()
    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
