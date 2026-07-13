"""Task 4: Load the CSV into MySQL (insert new rows, update existing ones).

The "reservations" table already exists (see sql/init.sql - it's created
automatically when the database container first starts). Your job is only to
fill it with the rows from data/processed/reservations.csv.

reservation_id is the table's PRIMARY KEY, so MySQL supports doing an
insert-or-update in a single statement:

    INSERT INTO reservations (col1, col2, ...)
    VALUES (%s, %s, ...)
    ON DUPLICATE KEY UPDATE
        col2 = VALUES(col2),
        ...

Run it with:
    make run FILE=tasks/04_task.py

(Run Task 3 first if data/processed/reservations.csv doesn't exist yet.)

Afterwards, open http://localhost:8081 (Adminer), log into the "db" server
with the credentials from your .env file, and check the "reservations" table.

TODO:
1. Write the INSERT ... ON DUPLICATE KEY UPDATE statement (see hint above).
2. For each row, execute it with the row's values.
3. Commit once you're done inserting all rows.
"""

from __future__ import annotations

import csv
import os

import mysql.connector
from dotenv import load_dotenv

CSV_PATH = "data/processed/reservations.csv"


def read_csv_rows() -> list[dict]:
    with open(CSV_PATH, "r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def connect():
    load_dotenv()

    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
    )


def upsert_reservations(rows: list[dict]) -> None:
    connection = connect()
    cursor = connection.cursor()

    try:
        # TODO: for each row in `rows`, execute an INSERT ... ON DUPLICATE KEY UPDATE
        # statement with that row's values, then commit once all rows are done.
        raise NotImplementedError("Task 4: insert/update each row into MySQL.")
    finally:
        cursor.close()
        connection.close()


def main() -> None:
    rows = read_csv_rows()
    upsert_reservations(rows)
    print(f"Upserted {len(rows)} rows into MySQL.")


if __name__ == "__main__":
    main()
