#!/usr/bin/python3


"""Here we are going to a perimeter and an area to the Rectangle"""


class Rectangle:

    """Defining Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of Data"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Accessing width (Getter method)"""
        return self.__width

    @width.setter
    def width(self, value):
        """Defining width by setter methods"""
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
        """Defining height by setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defining Area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Defining the Perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
