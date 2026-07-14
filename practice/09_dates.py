"""Practice 9: Dates.

Read first: Python Dates.
https://www.w3schools.com/python/default.asp

Run it with:
    make run FILE=practice/09_dates.py
"""

from datetime import date

# Example
arrival = date.fromisoformat("2026-07-13")
departure = date.fromisoformat("2026-07-16")

print(departure >= arrival)

# Exercise 1: compute the number of nights between `arrival` and
# `departure` ((departure - arrival).days) and print it.
# TODO: your code here

# Exercise 2: given the list of dates below, print them sorted from
# earliest to latest using sorted().
some_dates = [
    date.fromisoformat("2026-08-01"),
    date.fromisoformat("2026-07-20"),
    date.fromisoformat("2026-07-25"),
]
# TODO: your code here

# Exercise 3: check whether today's date (date.today()) falls between
# `arrival` and `departure` (inclusive), and print True/False.
# TODO: your code here
