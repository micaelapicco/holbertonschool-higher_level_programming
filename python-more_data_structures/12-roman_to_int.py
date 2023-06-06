#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) == int:
        return 0
    converter = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    counter = 0
    for i in roman_string:
        if i in converter.keys():
            if counter < converter[i]:
                counter *= -1
            counter += converter[i]
        else:
            return (0)
    return (counter)
