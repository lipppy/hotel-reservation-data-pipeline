# Project Flow: Hotel Reservation REST API

## Context

This is a one-week internship task, Monday to Friday. The goal by **Friday** is a
working REST API that serves hotel reservation data to an already-built frontend
(`index.html`).

You are not designing the architecture — that part is intentionally decided for
you, and it is a bit unusual on purpose. The point of this week is to get hands-on
practice with a few core building blocks of software development:

- calling an external API,
- reading and writing files (JSON and CSV),
- storing and updating data in a database,
- building a REST API endpoint,
- connecting that endpoint to a real, working frontend.

Don't worry about making this "clean" or "production-grade". A real system would
not be built this way. This version deliberately touches every piece by hand so
you see how each format and each layer works, before you ever use a framework or
library that would hide it from you.

## What already exists (you don't need to build this)

- `integrations/apaleo/client.py` — a ready-made client for the Apaleo hotel
  system API. You will **use** it, not build it.
- `index.html` — the finished frontend. It already expects a backend at
  `/api/reservations` and knows how to display whatever JSON that endpoint
  returns. You don't need to touch this file.
- `docker-compose.yml` — starts everything you need: a MySQL database (`db`), a
  database browser (`adminer`, at `http://localhost:8081`), your backend API
  (`api`, at `http://localhost:5000`), and the frontend (`web`, at
  `http://localhost:8080`).
- `sql/init.sql` — creates the `reservations` table in MySQL automatically the
  first time the database container starts. You don't create tables yourself,
  only insert/update rows in the table that's already there.
- `.env` — holds the Apaleo credentials and the MySQL connection details
  (host, user, password, database). Your code reads these with the
  `python-dotenv` package, never hard-code them.

## The flow you are building

Everything below happens **inside a single Flask endpoint**, step by step, in
this order:

```
1. Call the Apaleo API                (integrations/apaleo/client.py)
        ↓
2. Save the full JSON response to a file
        ↓
3. Pick out only the fields we need and save them to a CSV file
        ↓
4. Read the CSV file back
        ↓
5. Insert new rows / update existing rows in the MySQL "reservations" table
        ↓
6. Query MySQL again for the hotel + date range that was asked for
        ↓
7. Return the result as JSON
        ↓
8. index.html renders it
```

Yes, step 2-3 (save to a file) followed by step 4 (immediately read the same
file back) is a bit artificial — a real system usually wouldn't bother writing
that file at all. It's here so you get to practice both writing and reading
JSON and CSV files. That is the whole point of this project: it's a forced,
simplified version of a real pipeline so you touch every part of it yourself.

The single REST endpoint you're building takes these inputs from the frontend
(as query parameters on the URL):

- `hotelCode` — a 3-letter hotel code (e.g. `BER`)
- `from` / `to` — a date range, at most **7 days**

It must reject anything that doesn't match those rules (wrong code length,
range longer than a week, etc.) with a clear error message, and otherwise
return the matching reservations as JSON.

## Task-by-task plan

Work through these in order. Each one is a small Python script in `tasks/`
that you run and edit through Docker:

```bash
make run FILE=tasks/01_task.py
```

Each file has a docstring at the top explaining exactly what to do, and `TODO`
comments marking where your code goes. Do not move to the next task until the
current one runs without errors and produces the output described in it.

1. **`tasks/01_task.py`** — Initialize the Apaleo client and call the
   reservations endpoint for one hotel and one date range. Print the result.
   *You practice: reading environment variables, calling a function, reading a
   JSON response.*
2. **`tasks/02_task.py`** — Take that same API response and save it, unchanged,
   into a JSON file. *You practice: opening files for writing, `json.dump`.*
3. **`tasks/03_task.py`** — From the same data, pick only the fields we actually
   need (reservation id, hotel code, arrival, departure, adults, children,
   status) and save them into a CSV file, one row per reservation. *You
   practice: reading JSON, the `csv` module, choosing which data matters.*
4. **`tasks/04_task.py`** — Read that CSV file back, connect to MySQL using the
   values from `.env`, and for each row either INSERT it (new reservation) or
   UPDATE it (already exists). *You practice: database connections, SQL
   INSERT/UPDATE, commit.*
5. **`tasks/05_task.py`** — Query MySQL for reservations matching a given hotel
   code and date range, and print the result as JSON. *You practice: SQL
   `SELECT ... WHERE`, turning database rows into JSON.*
6. **`api.py`** — Combine everything from tasks 1-5 into the real
   `/api/reservations` endpoint: read `hotelCode`/`from`/`to` from the request,
   validate them, run the full flow, and return JSON. This is the final
   deliverable — once this works, open `http://localhost:8080` and the
   dashboard should show real data.

If you finish early: pull the repeated logic out of the endpoint into small,
named functions (e.g. `fetch_from_apaleo(...)`, `save_json(...)`,
`save_csv(...)`, `upsert_reservations(...)`, `query_reservations(...)`). How
you split it up is up to you — there's no single right answer here.

## Daily checkpoint suggestion

- **Monday**: Task 1-2 (Apaleo call + JSON file).
- **Tuesday**: Task 3 (CSV file).
- **Wednesday**: Task 4 (MySQL insert/update). Use Adminer
  (`http://localhost:8081`) to check the data actually landed in the table.
- **Thursday**: Task 5 (MySQL query) + start Task 6 (Flask endpoint).
- **Friday**: Finish Task 6, test end-to-end from `http://localhost:8080`.

If you get stuck on an error you don't understand, or progress stalls for more
than 20-30 minutes, ask for help instead of guessing.

---

## Appendix: Python basics reference

If any of the topics above feel unfamiliar, use the W3Schools Python tutorial
as a reference. Do not complete the entire tutorial — only the sections below,
and only as much as you need to get unstuck on the tasks above.

Main tutorial:

https://www.w3schools.com/python/default.asp

### 1. Getting Started

Read: Python Intro, Python Get Started, Python Syntax, Python Output, Python
Comments.

```python
print("Hotel reservation project")
```

Practice: [`practice/01_getting_started.py`](practice/01_getting_started.py)

### 2. Variables and Basic Data Types

Read: Python Variables, Python Data Types, Python Numbers, Python Casting,
Python Strings, Python Booleans.

```python
apaleo_id = "RES-12345"
adults = 2
children = 1
is_cancelled = False

total_guests = adults + children
print(total_guests)
```

Practice: [`practice/02_variables_and_data_types.py`](practice/02_variables_and_data_types.py)

### 3. Lists and Dictionaries

Read: Python Lists, Access List Items, Add List Items, Loop Lists, Python
Dictionaries, Access Dictionary Items, Change Dictionary Items, Loop
Dictionaries.

```python
reservation = {
    "apaleo_id": "RES-12345",
    "adults": 2,
    "children": 1,
}

reservations = [reservation]

for item in reservations:
    print(item["apaleo_id"])
```

Skip tuples and sets unless needed later.

Practice: [`practice/03_lists_and_dictionaries.py`](practice/03_lists_and_dictionaries.py)

### 4. Conditions and Loops

Read: Python If...Else, Comparison Operators, Logical Operators, Python For
Loops, Python Range.

```python
if reservation["adults"] < 0:
    print("Invalid number of adults")

for reservation in reservations:
    print(reservation)
```

Read `while` loops only if required.

Practice: [`practice/04_conditions_and_loops.py`](practice/04_conditions_and_loops.py)

### 5. Functions

Read: Python Functions, Python Arguments, Python Scope.

```python
def get_total_guests(reservation):
    return reservation["adults"] + reservation["children"]
```

Skip decorators, recursion, generators, `*args`, `**kwargs` and lambda
functions for now — except the route decorators Flask itself requires
(`@app.get(...)`), which you can copy without needing to fully understand
decorators yet.

Practice: [`practice/05_functions.py`](practice/05_functions.py)

### 6. Modules and Packages

Read: Python Modules, Python PIP, Python VirtualEnv.

```python
import csv
import json
from datetime import date
```

Practice: [`practice/06_modules_and_packages.py`](practice/06_modules_and_packages.py)

### 7. File Handling

Read: Python File Handling, Python Read Files, Python Write/Create Files.

```python
with open("data/example.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Deleting files is not required.

Practice: [`practice/07_file_handling.py`](practice/07_file_handling.py)

### 8. JSON

Read: Python JSON.

```python
import json

with open("data/reservations.json", "r", encoding="utf-8") as file:
    reservations = json.load(file)
```

Practice: [`practice/08_json.py`](practice/08_json.py)

### 9. Dates

Read: Python Dates.

```python
from datetime import date

arrival = date.fromisoformat("2026-07-13")
departure = date.fromisoformat("2026-07-16")

print(departure >= arrival)
```

Practice: [`practice/09_dates.py`](practice/09_dates.py)

### 10. Error Handling

Read: Python Try...Except, Python None.

```python
try:
    adults = int("2")
except ValueError:
    print("Invalid number")
```

Practice: [`practice/10_error_handling.py`](practice/10_error_handling.py)

### 11. String Formatting

Read: Python String Formatting.

```python
print(f"{apaleo_id}: {total_guests} guests")
```

Practice: [`practice/11_string_formatting.py`](practice/11_string_formatting.py)

### 12. HTTP Requests

Use the W3Schools Requests module reference:

https://www.w3schools.com/python/module_requests.asp

```python
import requests

response = requests.get("https://example.com/api/reservations", timeout=30)
response.raise_for_status()

data = response.json()
```

Use the real API only with the credentials and instructions provided by the
mentor.

Practice: [`practice/12_http_requests.py`](practice/12_http_requests.py)

### 13. Database Work

The W3Schools Python database tutorial mostly covers MySQL, which matches
this project (we use MySQL, not PostgreSQL) — but the general sequence is what
matters most:

- connect;
- create a cursor;
- execute SQL;
- fetch rows (for SELECT) or commit (for INSERT/UPDATE);
- close the connection.

Use the `mysql-connector-python` package, and read the connection details
(host, user, password, database) from `.env` via `python-dotenv` — never
hard-code them.

Practice: [`practice/13_database_work.py`](practice/13_database_work.py)

### Not Required for This Project

Skip these unless the mentor specifically asks for them: tuples, sets, match
statements, advanced `while` loops, iterators, generators, recursion, regular
expressions, classes and object-oriented programming, inheritance and
polymorphism, NumPy, Pandas, Matplotlib, machine learning, data structures and
algorithms.

### Recommended Working Method

For each topic:

1. Read the short W3Schools explanation.
2. Run its example.
3. Change the example.
4. Recreate the same idea using reservation data.
5. Add the result to the current task file.
6. Ask for help if an error is unclear or progress stops.

The goal is not to memorize Python. The goal is to use enough Python to build
the reservation REST API.
