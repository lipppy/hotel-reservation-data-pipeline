"""Practice 5: Functions.

Read first: Python Functions, Python Arguments, Python Scope. Skip
decorators, recursion, generators, *args/**kwargs and lambdas for now.
https://www.w3schools.com/python/default.asp

Run it with:
    make run FILE=practice/05_functions.py
"""

from __future__ import annotations

reservations = [
    {"apaleo_id": "RES-1", "adults": 2, "children": 0},
    {"apaleo_id": "RES-2", "adults": 1, "children": 1},
    {"apaleo_id": "RES-3", "adults": 0, "children": 2},
]


# Example
def get_total_guests(reservation: dict) -> int:
    return reservation["adults"] + reservation["children"]


# Exercise 1: write a function that returns False if a reservation has 0
# adults (a reservation always needs at least one adult), True otherwise.
def is_valid_reservation(reservation: dict) -> bool:
    # TODO: your code here
    raise NotImplementedError


# Exercise 2: write a function that returns the average total guests
# (adults + children) across a list of reservations, as a float.
def average_guests(reservation_list: list[dict]) -> float:
    # TODO: your code here
    raise NotImplementedError


# Exercise 3: write a function that returns a formatted string like
# "RES-1: 2 guests" for a single reservation.
def describe_reservation(reservation: dict) -> str:
    # TODO: your code here
    raise NotImplementedError


def main() -> None:
    for reservation in reservations:
        print(get_total_guests(reservation))
        print(is_valid_reservation(reservation))
        print(describe_reservation(reservation))

    print(average_guests(reservations))


if __name__ == "__main__":
    main()
