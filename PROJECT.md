# Python Learning Flow

Use the W3Schools Python tutorial as a reference while working on the hotel reservation data pipeline.

Main tutorial:

https://www.w3schools.com/python/default.asp

Do not complete the entire tutorial. Follow only the sections below, in this order.

---

## 1. Getting Started

Read:

- Python Intro
- Python Get Started
- Python Syntax
- Python Output
- Python Comments

Goal:

- Run a Python file.
- Use `print()`.
- Understand indentation and comments.

Practice:

```python
print("Hotel reservation project")
```

---

## 2. Variables and Basic Data Types

Read:

- Python Variables
- Python Data Types
- Python Numbers
- Python Casting
- Python Strings
- Python Booleans

Goal:

- Store reservation values.
- Understand strings, integers, floats and booleans.
- Convert CSV strings into numbers.

Practice:

```python
apaleo_id = "RES-12345"
adults = 2
children = 1
is_cancelled = False

total_guests = adults + children
print(total_guests)
```

---

## 3. Lists and Dictionaries

Read:

- Python Lists
- Access List Items
- Add List Items
- Loop Lists
- Python Dictionaries
- Access Dictionary Items
- Change Dictionary Items
- Loop Dictionaries

Goal:

- Represent one reservation as a dictionary.
- Represent multiple reservations as a list.

Practice:

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

---

## 4. Conditions and Loops

Read:

- Python If...Else
- Comparison Operators
- Logical Operators
- Python For Loops
- Python Range

Goal:

- Filter and validate reservations.
- Process multiple records.

Practice:

```python
if reservation["adults"] < 0:
    print("Invalid number of adults")

for reservation in reservations:
    print(reservation)
```

Read `while` loops only if required.

---

## 5. Functions

Read:

- Python Functions
- Python Arguments
- Python Scope

Goal:

- Split the program into small reusable steps.

Practice:

```python
def get_total_guests(reservation):
    return reservation["adults"] + reservation["children"]
```

Skip decorators, recursion, generators, `*args`, `**kwargs` and lambda functions for now.

---

## 6. Modules and Packages

Read:

- Python Modules
- Python PIP
- Python VirtualEnv

Goal:

- Import built-in modules.
- Install project dependencies.
- Understand why the project uses an isolated environment.

Practice:

```python
import csv
import json
from datetime import date
```

---

## 7. File Handling

Read:

- Python File Handling
- Python Read Files
- Python Write/Create Files

Goal:

- Read and write project files.

Practice:

```python
with open("data/example.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Deleting files is not required.

---

## 8. JSON

Read:

- Python JSON

Goal:

- Read API-like JSON data.
- Export processed reservation data.

Practice:

```python
import json

with open("data/reservations.json", "r", encoding="utf-8") as file:
    reservations = json.load(file)
```

---

## 9. Dates

Read:

- Python Dates

Goal:

- Parse and compare arrival and departure dates.

Practice:

```python
from datetime import date

arrival = date.fromisoformat("2026-07-13")
departure = date.fromisoformat("2026-07-16")

print(departure >= arrival)
```

---

## 10. Error Handling

Read:

- Python Try...Except
- Python None

Goal:

- Handle invalid files, dates and values without crashing unexpectedly.

Practice:

```python
try:
    adults = int("2")
except ValueError:
    print("Invalid number")
```

---

## 11. String Formatting

Read:

- Python String Formatting

Goal:

- Produce readable console messages and summaries.

Practice:

```python
print(f"{apaleo_id}: {total_guests} guests")
```

---

## 12. HTTP Requests

Use the W3Schools Requests module reference:

https://www.w3schools.com/python/module_requests.asp

Goal:

- Send a basic GET request.
- Read a JSON response.
- Check the response status.

Practice:

```python
import requests

response = requests.get("https://example.com/api/reservations", timeout=30)
response.raise_for_status()

data = response.json()
```

Use the real API only with the credentials and instructions provided by the mentor.

---

## 13. Database Work

The W3Schools Python database tutorial focuses mainly on MySQL, so use it only to understand the general sequence:

- connect;
- create a cursor;
- execute SQL;
- fetch rows;
- commit changes;
- close the connection.

For this project, use the PostgreSQL examples and helper code provided in the repository.

Do not copy MySQL-specific connection code into the project.

---

## Optional Exercises

After each important section, complete one or two W3Schools exercises.

Prioritize exercises for:

- variables;
- strings;
- lists;
- dictionaries;
- `if`;
- `for`;
- functions;
- file handling;
- JSON;
- exceptions.

Do not spend time completing every quiz or code challenge.

---

## Not Required for This Project

Skip these unless the mentor specifically asks for them:

- tuples;
- sets;
- match statements;
- advanced `while` loops;
- iterators;
- generators;
- decorators;
- recursion;
- regular expressions;
- classes and object-oriented programming;
- inheritance and polymorphism;
- NumPy;
- Pandas;
- Matplotlib;
- machine learning;
- data structures and algorithms.

---

## Recommended Working Method

For each topic:

1. Read the short W3Schools explanation.
2. Run its example.
3. Change the example.
4. Recreate the same idea using reservation data.
5. Add the result to the project.
6. Ask for help if an error is unclear or progress stops.

The goal is not to memorize Python. The goal is to use enough Python to build the reservation data pipeline.
