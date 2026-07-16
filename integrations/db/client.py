"""Slim MySQL client for the "reservations" table.

Used by the demo endpoint (`/api/reservations-demo` in api.py) to serve real
rows from MySQL, parametrized by hotel code and an optional date range. The
table itself is created and seeded by sql/init.sql.
"""

from __future__ import annotations

import datetime
import os

import mysql.connector
from dotenv import load_dotenv


def connect():
    load_dotenv()

    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
    )


def _normalize_value(value):
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    return value


def _rows_to_dicts(cursor) -> list[dict]:
    columns = [column[0] for column in cursor.description]
    return [
        {column: _normalize_value(value) for column, value in zip(columns, row)}
        for row in cursor.fetchall()
    ]


UPSERT_FIELDS = [
    "reservation_id",
    "property_id",
    "arrival",
    "departure",
    "adults",
    "children",
    "status",
]


def upsert_reservations(records: list[dict]) -> int:
    """Insert new reservations, or update existing ones (matched by
    reservation_id), in the "reservations" table.

    Accepts the shape integrations.apaleo.get_reservations returns (extra
    keys, e.g. updated_at from integrations.db.get_reservations itself, are
    ignored - only UPSERT_FIELDS are written). Returns the number of rows
    upserted.
    """
    if not records:
        return 0

    assignments = ", ".join(
        f"{column} = VALUES({column})" for column in UPSERT_FIELDS if column != "reservation_id"
    )
    query = (
        f"INSERT INTO reservations ({', '.join(UPSERT_FIELDS)}) "
        f"VALUES ({', '.join(['%s'] * len(UPSERT_FIELDS))}) "
        f"ON DUPLICATE KEY UPDATE {assignments}"
    )

    connection = connect()
    cursor = connection.cursor()

    try:
        for record in records:
            cursor.execute(query, [record.get(column) for column in UPSERT_FIELDS])
        connection.commit()
        return len(records)
    finally:
        cursor.close()
        connection.close()


def get_reservations(
    property_id: str,
    date_from: str | None = None,
    date_to: str | None = None,
) -> list[dict]:
    """Query reservations for one hotel, optionally restricted to a date range.

    Without date_from/date_to, every reservation for the property is
    returned. When given, they filter on arrival (inclusive on both ends).
    """
    query = "SELECT * FROM reservations WHERE property_id = %s"
    params: list[str] = [property_id]

    if date_from:
        query += " AND arrival >= %s"
        params.append(date_from)

    if date_to:
        query += " AND arrival <= %s"
        params.append(date_to)

    query += " ORDER BY arrival, reservation_id"

    connection = connect()
    cursor = connection.cursor()

    try:
        cursor.execute(query, params)
        return _rows_to_dicts(cursor)
    finally:
        cursor.close()
        connection.close()
