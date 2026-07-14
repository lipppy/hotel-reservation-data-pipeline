"""Practice 7: File Handling.

Read first: Python File Handling, Python Read Files, Python Write/Create
Files. Deleting files is not required.
https://www.w3schools.com/python/default.asp

Run it with:
    make run FILE=practice/07_file_handling.py
"""

# Example
with open("data/example.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

# Exercise 1: write your name into "data/practice_output.txt" using "w" mode
# (this creates the file if it doesn't exist, or overwrites it if it does).
# TODO: your code here

# Exercise 2: open "data/practice_output.txt" again, this time in "a"
# (append) mode, and add a second line to it without erasing the first.
# TODO: your code here

# Exercise 3: open "data/practice_output.txt" in "r" mode and print its
# contents, so you can check both lines are there.
# TODO: your code here
