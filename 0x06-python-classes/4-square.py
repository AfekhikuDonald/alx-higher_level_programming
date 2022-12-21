#!/usr/bin/python3
# 4-square.py
"""Creates a square."""


class Square:
    """Defines the square."""

    def __init__(self, size=0):
        """Initialise the class.
        Args:
            Size : the size of the square.
        """
        self.__size = size

    @property
    def size(self):
         """Properties for the length of a sise of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
         """Defines the area of the square.

        Returns: 
            The square of the size."""
        return self.__size ** 2
