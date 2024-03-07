#!/usr/bin/python3


"""Here we are going to Define Square based on 4-square.py"""


class Square:

    """We are going to Define Square"""

    def __init__(self, size=0):
        """we are going to initialize Square and Describe size"""
        self.__size = size

    @property
    def size(self):
        """Defining how to find size and returning it by getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Ensuring that Size is greater than 0"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """We are going to Define area and return it"""
        return self.__size ** 2

    def my_print(self):
        """We are going to prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print("#" * self.__size)
            return
