"""Practice 4: Conditions and Loops.

Read first: Python If...Else, Comparison Operators, Logical Operators,
Python For Loops, Python Range. Read `while` loops only if you're curious.
https://www.w3schools.com/python/default.asp

Run it with:
    make run FILE=practice/04_conditions_and_loops.py
"""

reservations = [
    {"apaleo_id": "RES-1", "adults": 2, "children": 0},
    {"apaleo_id": "RES-2", "adults": 0, "children": 1},
    {"apaleo_id": "RES-3", "adults": 1, "children": 2},
]

# Example
for reservation in reservations:
    if reservation["adults"] < 1:
        print(f"{reservation['apaleo_id']}: invalid, no adults")
    else:
        print(f"{reservation['apaleo_id']}: OK")

# Exercise 1: use range() to print the numbers 1 to 5 (one per line) - these
# represent night 1, night 2, ... of a stay.
# TODO: your code here

# Exercise 2: loop over `reservations` and count how many have children > 0.
# Print the final count.
# TODO: your code here

# Exercise 3: loop over `reservations` and print the apaleo_id of the one
# with the most total guests (adults + children). You can do this by keeping
# track of the best one seen so far as you loop.
# TODO: your code here
