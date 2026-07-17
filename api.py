"""Placeholder backend API for the reservation dashboard (index.html).

Run with: flask --app api run --host 0.0.0.0 --port 5000
"""

from __future__ import annotations

import datetime
import json
import logging

from flask import Flask, jsonify, request

from integrations.apaleo import get_reservations as get_api_reservations
from integrations.db import get_reservations as get_db_reservations
from integrations.db import upsert_reservations
from helpers.export import dump_to_json, dump_to_csv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    force=True,
)

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

app = Flask(__name__)

DEMO_HOTEL_CODES = ["BER", "VIE", "MUC"]
MAX_RANGE_DAYS = 7


@app.get("/api/playground")
def get_playground():
    """
    A simple test endpoint to confirm the backend is running.

    You can see me in your browser at http://localhost:5000/api/playground,
    and you can see me in the logs with `docker compose logs -f api`.
    I don't do anything useful.
    """
    print("Someone called /api/playground!sadsd", flush=True)
    log.info("Someone called /api/playground!")
    return jsonify({"message": "Hello from the backend!"})


@app.get("/api/reservations")
def get_reservations():
    """Get reservations from Apaleo API via MySQL database."""
    # Everything for this endpoint goes inside this function - follow the
    # checkpoints below in order. There are "TRY IT" checkpoints along the
    # way so you can see it working before you move on.
    #
    # This is still the FULL pipeline from PROJECT.md, steps 1-7, happening
    # live on every request:
    #   call Apaleo -> save JSON -> save CSV -> upsert MySQL -> query MySQL
    #   -> return JSON
    # Yes, that means the request you're about to build calls the real
    # Apaleo API and touches disk and the database every single time someone
    # loads the dashboard. That is deliberately wasteful for a real system -
    # see PROJECT.md's "flow you are building" section for why it's done
    # this way here anyway.
    #
    # What changed: you're no longer building each layer by hand. Every layer
    # (call Apaleo, save JSON, save CSV, upsert MySQL, query MySQL) is now a
    # single pre-built helper, already imported at the top of this file:
    #   get_api_reservations(property_id, date_from, date_to)  -> list[dict]
    #   dump_to_json(records, property_id, date_from, date_to) -> path written
    #   dump_to_csv(records, property_id, date_from, date_to)  -> path written
    #   upsert_reservations(records)                           -> rows upserted
    #   get_db_reservations(property_id, date_from, date_to)   -> list[dict]
    # Your job here is to CALL these five, in the right order, with the
    # right arguments - not to reimplement what they already do.

    # --- Part A: read and validate the input --------------------------------

    # 1. Read hotelCode, from and to off the request:
    #    request.args.get("hotelCode"), request.args.get("from"),
    #    request.args.get("to").



    # 2. TRY IT: add a temporary print(hotel_code, date_from, date_to), then
    #    open
    #    http://localhost:5000/api/reservations?hotelCode=BER&from=2026-07-01&to=2026-07-07
    #    (saving the file reloads the server automatically). Check
    #    `docker compose logs -f api` and confirm the three values printed
    #    are what you'd expect. Remove the print once it works.



    # 3. Check that hotelCode was actually provided and is exactly 3
    #    characters long. If not, return early with
    #    jsonify({"error": "..."}), 400 - don't continue to the rest of the
    #    function. (get_reservations_demo below does the same shape of check
    #    against a fixed list of demo codes, instead of "any 3 letters".)



    # 4. Check that from and to were both provided. If either is missing,
    #    return the same kind of 400 error.



    # 5. TRY IT: reload the URL without hotelCode
    #    (http://localhost:5000/api/reservations) and confirm you get your
    #    own error message back as JSON, instead of a crash page.



    # 6. Work out how many days lie between from and to, and check it's
    #    MAX_RANGE_DAYS or fewer (see the footer note in index.html: "range
    #    <= 7 days"). Return a 400 error if the range is too big.



    # --- Part B: fetch, save, upsert, re-query ------------------------------

    # 7. Call get_api_reservations(hotel_code, date_from, date_to). It
    #    already talks to the real Apaleo API and filters by property and by
    #    stay date range - the rows it hands back are already shaped like
    #    the "reservations" table (reservation_id, property_id, arrival,
    #    departure, adults, children, status). Store the result, e.g. as
    #    `reservations`.



    # 8. TRY IT: temporarily print(reservations) or its length, reload the
    #    URL, and confirm real data came back from Apaleo for that
    #    hotel/date range. Remove the print once it works.



    # 9. Call dump_to_json(reservations, hotel_code, date_from, date_to) and
    #    dump_to_csv(reservations, hotel_code, date_from, date_to). Both
    #    create their own folder if needed and return the path they wrote -
    #    the same fetch is now saved as both a data/raw/*.json file and a
    #    data/processed/*.csv file, no manual file handling required.



    # 10. TRY IT: open the two files these just wrote (their names encode
    #     the hotel code and date range you requested) and confirm the
    #     content matches what Apaleo sent back.



    # 11. Call upsert_reservations(reservations) to insert new rows, or
    #     update existing ones (matched by reservation_id), in MySQL.



    # 12. TRY IT: open http://localhost:8081 (Adminer), log in with the
    #     credentials from your .env file, and check the "reservations"
    #     table now has rows in it.



    # 13. Call get_db_reservations(hotel_code, date_from, date_to) to read
    #     back exactly the hotel/date range that was asked for. Store it,
    #     e.g. as `records`.



    # --- Part C: respond -----------------------------------------------------

    # 14. Return jsonify(records).



    # 15. TRY IT: reload
    #     http://localhost:5000/api/reservations?hotelCode=BER&from=2026-07-01&to=2026-07-03
    #     (use a hotel/date range you know has real Apaleo data) and confirm
    #     you get real reservations back as JSON. Then open
    #     http://localhost:8080, switch "Source" to "Live API", and watch
    #     your own data show up in the dashboard - that's the whole pipeline,
    #     end to end.



    return jsonify({})


@app.get("/api/reservations-demo")
def get_reservations_demo():
    """Get demo reservations (BER, VIE, MUC) from MySQL, seeded by sql/init.sql.

    Mirrors the query contract /api/reservations will eventually have:
    hotelCode + from + to, with the same <= MAX_RANGE_DAYS-day range limit.
    """
    property_id = request.args.get("hotelCode")
    date_from = request.args.get("from")
    date_to = request.args.get("to")

    if property_id not in DEMO_HOTEL_CODES:
        return jsonify({"error": f"Demo data for {property_id} not available."}), 400

    if not date_from or not date_to:
        return jsonify({"error": "Both 'from' and 'to' are required."}), 400

    try:
        parsed_from = datetime.date.fromisoformat(date_from)
        parsed_to = datetime.date.fromisoformat(date_to)
    except ValueError:
        return (
            jsonify({"error": "'from' and 'to' must be dates in YYYY-MM-DD format."}),
            400,
        )

    if parsed_from > parsed_to:
        return (
            jsonify({"error": "The start date cannot be later than the end date."}),
            400,
        )

    if (parsed_to - parsed_from).days > MAX_RANGE_DAYS - 1:
        return (
            jsonify(
                {"error": f"The date range can span at most {MAX_RANGE_DAYS} days."}
            ),
            400,
        )

    records = get_db_reservations(property_id, date_from, date_to)
    return jsonify(records)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
