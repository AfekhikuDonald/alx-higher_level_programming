#!/usr/bin/python3
# 2-square.py
""" create a square class"""


class Square:
    """ define the square"""

    def __init__(self, size=0):
        """initialize the square attributes
        Args:
            size : the size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
