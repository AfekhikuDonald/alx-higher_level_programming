#!/usr/bin/python3
# 5-square.py
"""create a class"""


class Square:
    """ defines a square"""

    def __init__(self, size=0):
          """initialise the class
        Args:
            size : the size of the square
        """
        self.size = size

    @property
    def size(self):
         """Properties for the length of a sise of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        return self._size

    @size.setter
    def size(self, value):
        """ setter function for private attribute size
            Args:
                value: value to be set.
            Returns:
                nothing.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
         """defines the area of the square

        Returns: the square of the size"""
        return self.size ** 2

    def my_print(self):
        """prints the square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)

