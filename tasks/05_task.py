"""Task 5: Query MySQL for one hotel and one date range, return JSON.

This is the core logic that Task 6 (the real /api/reservations endpoint in
api.py) will use. Given a 3-letter hotel code and a date range, find the
matching rows in the "reservations" table and turn them into a list of plain
Python dicts, ready to be converted to JSON.

Run it with:
    make run FILE=tasks/05_task.py

(Run Task 4 first so there's actually data in the table.)

TODO:
1. Write a SELECT statement: rows where property_id = %s and arrival is
   between the two given dates (inclusive).
2. Execute it with (PROPERTY_ID, DATE_FROM, DATE_TO).
3. Use cursor.fetchall() to get the rows, and cursor.description to get the
   column names, then zip them together into a list of dicts.
"""

from __future__ import annotations

import json
import os

import mysql.connector
from dotenv import load_dotenv

PROPERTY_ID = "BER"
DATE_FROM = "2026-07-01"
DATE_TO = "2026-07-07"


def connect():
    load_dotenv()

    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
    )


def rows_to_dicts(cursor) -> list[dict]:
    """Turn cursor.fetchall() tuples into a list of {column_name: value} dicts."""

    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def query_reservations(property_id: str, date_from: str, date_to: str) -> list[dict]:
    connection = connect()
    cursor = connection.cursor()

    try:
        # TODO: execute a SELECT ... WHERE property_id = %s AND arrival BETWEEN %s AND %s
        # statement here, then return rows_to_dicts(cursor).
        raise NotImplementedError("Task 5: query MySQL and return the matching rows.")
    finally:
        cursor.close()
        connection.close()


def main() -> None:
    results = query_reservations(PROPERTY_ID, DATE_FROM, DATE_TO)
    print(json.dumps(results, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
