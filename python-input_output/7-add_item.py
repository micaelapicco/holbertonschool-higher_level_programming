#!/usr/bin/python3
"""
Task 7: Write a script that adds all arguments to a Python list,
and then save them to a file
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
file = "add_item.json"
#with open(file, 'a', encoding="utf-8") as f:
if os.path.exist(file):
    my_list = load_from_json_file(file) + args[1:]
    
else:
    my_list = []
    
save_to_json_file(my_list, file)

# 1: os, library "path"