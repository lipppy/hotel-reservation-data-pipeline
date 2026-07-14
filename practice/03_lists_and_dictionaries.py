"""Practice 3: Lists and Dictionaries.

Read first: Python Lists, Access List Items, Add List Items, Loop Lists,
Python Dictionaries, Access Dictionary Items, Change Dictionary Items, Loop
Dictionaries. Skip tuples and sets for now.
https://www.w3schools.com/python/default.asp

Run it with:
    make run FILE=practice/03_lists_and_dictionaries.py
"""

# Example
reservation = {
    "apaleo_id": "RES-12345",
    "adults": 2,
    "children": 1,
}

reservations = [reservation]

for item in reservations:
    print(item["apaleo_id"])

# Exercise 1: add a second reservation dict (with different values) to the
# `reservations` list using reservations.append(...).
# TODO: your code here

# Exercise 2: loop over `reservations` and print each one's apaleo_id
# together with its total guests (adults + children).
# TODO: your code here

# Exercise 3: loop over `reservations` and print only the ones where
# adults is 2 or more.
# TODO: your code here
