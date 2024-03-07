#!/usr/bin/python3


"""This module contains also area modifier of the square"""


class Square:
    """We are going to define square"""

    def __init__(self, size=0):

        """we are going to explaining Data"""

        self.__size = size
        if type(size) != int:
            raise TypeError("size must an integer")
        if size < 0 :
            raise ValueError("size must be >= 0")

    def area(self):
        
        """we are going to return the area of square"""
        
        return self.__size**2
