#!/usr/bin/python3
"""
Task 2: Write a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """write a str to a text"""
    with open(filename, 'a', encoding="utf-8") as file:
        return (file.write(text))

# 1 - with close automatically the file
# 2 - return write automatically count number of characters
# 3 - a, append, no rewrite over text
