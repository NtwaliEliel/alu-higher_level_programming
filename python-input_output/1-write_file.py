#!/usr/bin/python3


"""NO module Imported"""


def write_file(filename="", text=""):
    """Writing"""
    with open(filename, mode='w', encoding="utf8") as f:
        return f.write(text)
