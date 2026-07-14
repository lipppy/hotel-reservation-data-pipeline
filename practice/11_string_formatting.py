"""Practice 11: String Formatting.

Read first: Python String Formatting.
https://www.w3schools.com/python/default.asp

Run it with:
    make run FILE=practice/11_string_formatting.py
"""

apaleo_id = "RES-12345"
adults = 2
children = 1
total_guests = adults + children
nightly_rate = 89.5

# Example
print(f"{apaleo_id}: {total_guests} guests")

# Exercise 1: print nightly_rate formatted as currency with exactly 2
# decimal places, e.g. "Rate: 89.50 EUR" (hint: f"{value:.2f}").
# TODO: your code here

# Exercise 2: build and print a summary string like
# "BER: 2026-07-01 -> 2026-07-05 (3 guests)" using an f-string, for the
# values below.
property_id = "BER"
arrival = "2026-07-01"
departure = "2026-07-05"
# TODO: your code here

# Exercise 3: print each hotel code below right-aligned to a width of 5
# characters (hint: f"{code:>5}").
hotel_codes = ["BER", "MUC", "HAM"]
# TODO: your code here
