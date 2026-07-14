"""Practice 14: Testing.

Read first: the pytest "Get Started" guide - just enough to see what a test
function looks like and what `assert` does.
https://docs.pytest.org/en/stable/getting-started.html

pytest works differently from the other practice/ files: it doesn't run the
file top to bottom. Instead it looks for functions whose name starts with
test_, calls each one, and a test passes as long as nothing inside it raises
an error - including a failed `assert`. Running `python practice/14_testing.py`
directly does nothing useful; pytest is what finds and calls the test_
functions (see pytest.ini - it's set up to also look inside practice/ for
files ending in _testing.py, not just the usual test_*.py).

Run it with:
    make test

That runs every test in the project (this file included). To run only this
file: `pytest practice/14_testing.py`.
"""

from __future__ import annotations

import pytest


# The code under test - same helper as practice/05_functions.py.
def total_guests(adults: int, children: int) -> int:
    return adults + children


# Example: a test function. pytest calls this because its name starts with
# test_. No print, no return value - if the assert doesn't raise, it passes.
def test_total_guests_adds_adults_and_children():
    assert total_guests(2, 1) == 3


# Exercise 1: write a test asserting total_guests(0, 0) equals 0.
def test_total_guests_with_no_guests():
    raise NotImplementedError  # TODO: replace this with a real assert


# The code under test for exercises 2-3: a reservation always needs at
# least one adult.
def is_valid_reservation(adults: int) -> bool:
    return adults > 0


# Exercise 2: write a test asserting is_valid_reservation(2) is True.
def test_is_valid_reservation_accepts_at_least_one_adult():
    raise NotImplementedError  # TODO: your code here


# Exercise 3: write a test asserting is_valid_reservation(0) is False.
def test_is_valid_reservation_rejects_zero_adults():
    raise NotImplementedError  # TODO: your code here


# Exercise 4: pytest.raises checks that a specific error actually happens -
# useful for confirming bad input gets rejected instead of silently accepted.
# Inside this test, wrap int("not-a-number") in
# `with pytest.raises(ValueError):` to confirm it raises ValueError.
def test_int_conversion_raises_on_bad_input():
    raise NotImplementedError  # TODO: your code here
