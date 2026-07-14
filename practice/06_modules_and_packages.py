"""Practice 6: Modules and Packages.

Read first: Python Modules, Python PIP, Python VirtualEnv.
https://www.w3schools.com/python/default.asp

Run it with:
    make run FILE=practice/06_modules_and_packages.py
"""

import json
from datetime import date

# Example: these are all built-in modules, no installation needed.
print(f"Today is {date.today()}")
print(json.dumps({"today": str(date.today())}))

# Exercise 1: import the "os" module and print the current working directory
# with os.getcwd().
# TODO: your code here

# Exercise 2: import the "random" module and print a random integer between
# 1 and 10 with random.randint(1, 10).
# TODO: your code here

# Exercise 3 (no code, just a comment): this project lists its dependencies
# in requirements.txt and installs them inside a Docker container instead of
# directly on your computer. Write 1-2 sentences below explaining, in your
# own words, why that's useful (hint: see "What is a virtual environment?"
# in FAQ.md).
# TODO: your answer as a comment here
