#!/usr/bin/python3


"""No module imported"""
import json


def to_json_string(my_obj):
    """Returning JSON"""
    return json.dumps(my_obj, ensure_ascii=False)
