#!/usr/bin/python3


"""No module imported"""


def append_write(filename="", text=""):
    """Appending"""
    with open(filename, mode='a', encoding="utf8") as f:
        return f.write(text)
