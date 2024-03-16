#!/usr/bin/python3


"""args imported"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

filename = "add_item.json"
if path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []
for x in range(1, len(argv)):
    my_list.append(argv[x])
save_to_json_file(my_list, filename)
