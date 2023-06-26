#!/usr/bin/python3
"""
Task 1: Write a function that writes a string to a
text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """write a str to a text"""
    with open(filename, 'w', encoding="utf-8") as file:
        return (file.write(text))

# 1 - with close automatically the file
# 2 - return write automatically count number of characters
