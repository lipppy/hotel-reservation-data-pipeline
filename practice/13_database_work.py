"""Practice 13: Database Work.

Read first: the W3Schools Python MySQL tutorial, just to see the general
sequence (connect, cursor, execute, fetch/commit, close) - this project uses
MySQL, so that part matches, but we use mysql-connector-python and read the
connection details from .env instead of hard-coding them.
https://www.w3schools.com/python/default.asp

This uses its own scratch table ("practice_notes") so it won't touch the
real "reservations" table used by the tasks/ pipeline.

Run it with:
    make run FILE=practice/13_database_work.py
"""

from __future__ import annotations

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


# Example: connect, create a scratch table if needed, insert one row, and
# read it back.
connection = connect()
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS practice_notes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        note VARCHAR(255) NOT NULL
    )
    """)
cursor.execute(
    "INSERT INTO practice_notes (note) VALUES (%s)", ("hello from practice",)
)
connection.commit()

cursor.execute("SELECT id, note FROM practice_notes")
print(cursor.fetchall())

# Exercise 1: insert two more rows into practice_notes with different note
# text, then commit.
# TODO: your code here

# Exercise 2: SELECT all rows from practice_notes again and print them, to
# confirm your two new rows are there.
# TODO: your code here

# Exercise 3: delete all rows from practice_notes (DELETE FROM
# practice_notes), commit, then SELECT again to confirm the table is empty.
# TODO: your code here

cursor.close()
connection.close()
