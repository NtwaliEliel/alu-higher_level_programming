#!/usr/bin/python3
import math


"""Math module for arthimetic operation"""


class MagicClass:
    
    """Defining MagicClass"""
    
    def __init__(self, radius=0):
        """Initializing Data"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Starting area"""
        return self.__radius**2 * math.pi

    def circumference(self):
        """Defining circumference"""
        return 2 * math.pi * self.__radius
