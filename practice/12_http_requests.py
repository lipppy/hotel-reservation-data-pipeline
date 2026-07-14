"""Practice 12: HTTP Requests.

Read first: the W3Schools Requests module reference.
https://www.w3schools.com/python/module_requests.asp

This uses https://example.com, a harmless public test page - not a real
hotel API. Use the real Apaleo API only with the credentials and
instructions provided by your mentor.

Run it with:
    make run FILE=practice/12_http_requests.py
"""

import requests

# Example
response = requests.get("https://example.com", timeout=30)
response.raise_for_status()

print(response.status_code)

# Exercise 1: print how many characters are in the page (len(response.text)).
# TODO: your code here

# Exercise 2: print the response's "Content-Type" header
# (response.headers.get("Content-Type")).
# TODO: your code here

# Exercise 3 (no code, just a comment): explain in 1-2 sentences what
# response.raise_for_status() does, and what would happen in this script if
# you removed that line and the request failed.
# TODO: your answer as a comment here
