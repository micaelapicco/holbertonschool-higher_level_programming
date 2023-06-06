#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return (None)
    else:
        max_v = 0
        key_new = ""
        for key in a_dictionary:
            if a_dictionary[key] > max_v:
                max_v = a_dictionary[key]
                key_new = key
    return (key_new)
