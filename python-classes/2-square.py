#!/usr/bin/python3


"""This module define size in square"""


class Square:
    """Here we are going to define square"""
    def __init__(self, size=0):
        """We are going to explain data and put error protections"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
