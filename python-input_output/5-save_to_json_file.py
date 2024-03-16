#!/usr/bin/python3


"""json imported"""
import json


def save_to_json_file(my_obj, filename):
    """Writing using json"""
    with open(filename, mode='w') as f:
        json.dump(my_obj, f, ensure_ascii=False)
