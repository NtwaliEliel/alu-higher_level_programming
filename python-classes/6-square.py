#!/usr/bin/python3


"""This module add position to Square based on 5-square.py"""


class Square:

    """Defining Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing Datas"""
        self.size = size
        self.position = position

    def area(self):
        """Describing area by returning it"""
        return self.__size**2

    @property
    def size(self):
        """Defining size by getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Verification of size by setter method"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Print the square with #"""
        if self.__size == 0:
            print("")
        else:
            for y in range(self.position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()

    @property
    def position(self):
        """Defining positive by returning it based to Getters method"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
