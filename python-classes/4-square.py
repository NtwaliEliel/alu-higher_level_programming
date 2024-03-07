#!/usr/bin/python3
"""This module Define square based on 3-square.py"""


class Square:
    """This Define Square"""

    def __init__(self, size=0):
        """This initialize Square and all arguments"""

        self.__size = size

    @property
    def size(self):
        """This finds size by getter methods"""
        return self.__size

    @size.setter
    def size(self, value):
        """This validate size by setter method"""
        self.__size = value

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """We are going to create an area for Square"""
        return self.__size ** 2
