#!/usr/bin/python3


"""7-base_geometry module is imported"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Rectangle class"""

    def __init__(self, width, height):
        """Instantiation"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
