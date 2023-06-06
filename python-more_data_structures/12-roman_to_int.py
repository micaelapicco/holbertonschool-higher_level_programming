#!/usr/bin/python3
def roman_to_int(roman_string):
    converter = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    counter = 0
    for i in roman_string:
        if i in converter.keys():
            if counter < converter[i]:
                counter *= -1
            counter += converter[i]
    return (counter)
