"""Practice 8: JSON.

Read first: Python JSON.
https://www.w3schools.com/python/default.asp

Run it with:
    make run FILE=practice/08_json.py

Uses the sample data in data/practice_reservations.json (a small, made-up
file - not real data, just for practice).
"""

import json

PRACTICE_PATH = "data/practice_reservations.json"

# Example
with open(PRACTICE_PATH, "r", encoding="utf-8") as file:
    reservations = json.load(file)

print(reservations)

# Exercise 1: print how many reservations the file contains (use len()).
# TODO: your code here

# Exercise 2: loop through `reservations` and print each one's apaleo_id
# together with its total guests (adults + children).
# TODO: your code here

# Exercise 3: build a new list containing only the reservations where
# is_cancelled is False, then write that list to
# "data/practice_reservations_filtered.json" with json.dump().
# TODO: your code here
