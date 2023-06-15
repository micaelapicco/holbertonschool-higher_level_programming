#!/usr/bin/python3
'''
5-text indentation - Module
'''


def text_indentation(text):
    '''
    prints a text with 2 new lines after each of these characters:
    ., ? and :
    '''
    if type(text) != str:
        raise TypeError("text must be a string")
    flag = 0
    for letter in range(len(text)):
        if text[letter] is '.' or text[letter] is '?' or text[letter] is ':':
            print(text[letter] + "\n")
            flag = 1
        if flag == 1:
            if text[letter + 1] == " ":
                continue
            flag = 0
        else:
            print(text[letter], end="")
