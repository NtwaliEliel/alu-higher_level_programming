#!/usr/bin/python3


"""No module Imported"""


class Rectangle:
    
    """Defining Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialization"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Accessing width by Getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Defining width by setter method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Accessing height by Getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Defining height by setter method"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defining area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Defining perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Creating String Representation of Rectangle"""
        s = ''
        if self.__width > 0 or self.__height > 0:
            for _ in range(self.__height):
                for _ in range(self.__width):
                    s += str(self.print_symbol)
                s += '\n'
        return s[: -1]

    def __repr__(self):
        """Conical string Represantation object"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Print a closure"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
