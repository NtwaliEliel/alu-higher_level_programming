#!/usr/bin/python3


"""JSON imported"""
import json


def load_from_json_file(filename):
    """Creating from JSON"""
    with open(filename) as f:
        return json.load(f)
