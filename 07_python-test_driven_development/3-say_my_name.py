#!/usr/bin/python3
'''
3- say my name - Module
'''


def say_my_name(first_name, last_name=""):
    """say the first name and the last name"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
