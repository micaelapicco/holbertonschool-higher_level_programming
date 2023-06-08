#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if (isinstance(roman_string, str) and roman_string):
        roman_string += "-"
        for i in range(len(roman_string) - 1):
            if roman_string[i] == 'I':
                if roman_string[i + 1] == 'V' or roman_string[i + 1] == 'X':
                    result -= 1
                else:
                    result += 1
            if roman_string[i] == 'V':
                result += 5
            if roman_string[i] == 'X':
                if roman_string[i + 1] == 'L' or roman_string[i + 1] == 'C':
                    result -= 10
                else:
                    result += 10
            if roman_string[i] == 'L':
                result += 50
            if roman_string[i] == 'C':
                result += 100
            if roman_string[i] == 'D':
                if roman_string[i + 1] == 'M':
                    result -= 500
                else:
                    result += 500
            if roman_string[i] == 'M':
                result += 1000
        roman_string = roman_string[:-1]
    return (result)
