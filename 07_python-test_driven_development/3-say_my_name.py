#!/usr/bin/python3
'''
Task 3: Write a function that prints My name is <first name> <last name>
'''


def say_my_name(first_name, last_name=""):
    """say the first name and the last name"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
