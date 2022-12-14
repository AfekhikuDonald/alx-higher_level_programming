#!/usr/bin/python3
# 3-python.py
"""creates a class"""


class Square:
    """define the class"""

    def __init__(self, size=0):
        """initialise the class
        Args:
            size : the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """defines the area of the square

        Returns: the square of the size"""
        return self.__size ** 2
