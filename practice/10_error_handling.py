"""Practice 10: Error Handling.

Read first: Python Try...Except, Python None.
https://www.w3schools.com/python/default.asp

Run it with:
    make run FILE=practice/10_error_handling.py
"""

from __future__ import annotations

# Example
try:
    adults = int("2")
except ValueError:
    print("Invalid number")

# Exercise 1: try converting the text below into an int inside a
# try/except. If it fails, print "Invalid number" instead of crashing.
guest_count_text = "abc"
# TODO: your code here


# Exercise 2: write a function safe_divide(a, b) that returns a / b, but if
# b is 0 it prints a friendly message and returns None instead of crashing.
def safe_divide(a: float, b: float) -> float | None:
    # TODO: your code here
    raise NotImplementedError


# Exercise 3: try opening a file that doesn't exist
# ("data/does_not_exist.txt") inside a try/except FileNotFoundError block,
# and print a friendly message instead of letting the program crash.
# TODO: your code here


if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
