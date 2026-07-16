"""Placeholder backend API for the reservation dashboard (index.html).

Run with: flask --app api run --host 0.0.0.0 --port 5000
"""

from __future__ import annotations

import datetime
import json
import logging

from flask import Flask, jsonify, request

from integrations.db import get_reservations as get_db_reservations

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
    # checkpoints below in order, one at a time. Don't skip ahead: each one
    # builds on the last, and there are "TRY IT" checkpoints along the way so
    # you can see it working before you move on.
    #
    # This isn't just "query the database" - it's the FULL pipeline from
    # PROJECT.md, steps 1-7, all happening live on every request:
    #   call Apaleo -> save JSON -> build CSV -> read CSV -> upsert MySQL ->
    #   query MySQL -> return JSON
    # Yes, that means the request you're about to build calls the real
    # Apaleo API and touches disk and the database every single time someone
    # loads the dashboard. That is deliberately wasteful for a real system -
    # see PROJECT.md's "flow you are building" section for why it's done
    # this way here anyway (so you practice every layer by hand).
    #
    # You'll need these imports at the top of the file: `request` from flask,
    # `os`, `csv`, `mysql.connector`, `load_dotenv` from dotenv, and
    # `ApaleoClient` from integrations.apaleo.

    # --- Part A: read and validate the input --------------------------------

    # 1. Read the hotelCode query param off the request:
    #    request.args.get("hotelCode")

    # 2. Read from and to the same way: request.args.get("from") and
    #    request.args.get("to").

    # 3. TRY IT: add a temporary print(hotelCode, ...) with all three values,
    #    then open
    #    http://localhost:5000/api/reservations?hotelCode=BER&from=2026-07-01&to=2026-07-03
    #    in your browser (saving the file reloads the server automatically).
    #    Check `docker compose logs -f api` and confirm the three values
    #    printed are what you'd expect. Remove the print once it works.

    # 4. Check that hotelCode was actually provided and is exactly 3
    #    characters long. If not, return early with
    #    jsonify({"error": "..."}), 400 - don't continue to the rest of the
    #    function.

    # 5. Check that from and to were both provided. If either is missing,
    #    return the same kind of 400 error.

    # 6. TRY IT: reload the URL without hotelCode
    #    (http://localhost:5000/api/reservations) and confirm you get your
    #    own error message back as JSON, instead of a crash page.

    # 7. Work out how many days lie between from and to, and check it's 7 or
    #    fewer (see the footer note in index.html: "range ≤ 7 days"). Return
    #    a 400 error if the range is too big.

    # --- Part B: call the Apaleo API (same as tasks/01_task.py) -------------

    # 8. Create an ApaleoClient(scope="reservations.read").

    # 9. Call client.get("/booking/v1/reservations", params=...) with
    #    propertyIds=[hotelCode], dateFilter="Stay", from=from_date,
    #    to=to_date.

    # 10. Turn the response into a Python object with response.json() and
    #     store it, e.g. as apaleo_data.

    # 11. TRY IT: temporarily print(apaleo_data) or its length, reload the
    #     URL, and confirm real reservation data came back from Apaleo for
    #     that hotel/date range. Remove the print once it works.

    # --- Part C: save the raw response to a file (same as tasks/02_task.py) -

    # 12. Make sure the "data/raw" folder exists:
    #     os.makedirs("data/raw", exist_ok=True)

    # 13. Write apaleo_data to data/raw/reservations.json with
    #     json.dump(..., indent=2, ensure_ascii=False).

    # 14. TRY IT: after a request, open data/raw/reservations.json in your
    #     editor and confirm it matches what Apaleo sent back.

    # --- Part D: build a CSV from it (same as tasks/03_task.py) -------------

    # 15. Read data/raw/reservations.json back with json.load(). Yes, this is
    #     the same data you just wrote in Part C - that's intentional, see
    #     the note at the top of this function and PROJECT.md.

    # 16. Get the list of reservations out of it (it may be a plain list, or
    #     wrapped under a "reservations" key - see get_reservation_list in
    #     tasks/03_task.py).

    # 17. Build one row dict per reservation with exactly these keys:
    #     reservation_id, property_id, arrival, departure, adults, children,
    #     status (mapped from the reservation's id, propertyId, arrival,
    #     departure, adults, children, status fields).

    # 18. Save the rows to data/processed/reservations.csv with
    #     csv.DictWriter (create the "data/processed" folder first).

    # 19. TRY IT: open data/processed/reservations.csv and confirm the rows
    #     and header look right.

    # --- Part E: load the CSV into MySQL (same as tasks/04_task.py) --------

    # 20. Read data/processed/reservations.csv back into a list of dicts
    #     with csv.DictReader.

    # 21. Call load_dotenv(), then open a MySQL connection - copy the
    #     connect() function from tasks/04_task.py.

    # 22. Get a cursor from the connection: cursor = connection.cursor()

    # 23. For each row, execute an
    #     INSERT ... ON DUPLICATE KEY UPDATE statement (see tasks/04_task.py
    #     for the exact SQL shape), then commit once all rows are done.

    # 24. TRY IT: open http://localhost:8081 (Adminer), log in with the
    #     credentials from your .env file, and check the "reservations"
    #     table now has rows in it.

    # --- Part F: query MySQL for what was asked (same as tasks/05_task.py) -

    # 25. Using the same cursor, write and execute a SELECT statement: rows
    #     where property_id = %s and arrival is between the from/to dates,
    #     with (hotelCode, from_date, to_date) as the values.

    # 26. Read the column names off cursor.description (one tuple per
    #     column; the name is the first item in each tuple).

    # 27. Zip the column names together with each row from
    #     cursor.fetchall() to build one dict per reservation - same idea as
    #     rows_to_dicts in tasks/05_task.py.

    # --- Part G: clean up and respond ---------------------------------------

    # 28. Close the cursor and the connection. Wrap steps 21-27 in a
    #     try/finally so they still close even if something above raises.

    # 29. Return jsonify(...) with your list of reservation dicts.

    # 30. TRY IT: reload
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
        return jsonify({"error": "'from' and 'to' must be dates in YYYY-MM-DD format."}), 400

    if parsed_from > parsed_to:
        return jsonify({"error": "The start date cannot be later than the end date."}), 400

    if (parsed_to - parsed_from).days > MAX_RANGE_DAYS - 1:
        return jsonify({"error": f"The date range can span at most {MAX_RANGE_DAYS} days."}), 400

    records = get_db_reservations(property_id, date_from, date_to)
    return jsonify(records)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
