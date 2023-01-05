#!/usr/bin/python3
"""defines a rectangle class."""


class Rectangle:
    """represents a rectangle."""
     def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """width getter"""
        return self.__width
    @widthsetter
    def width(self, value):
        """width setter"""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height
    @heightsetter
    def height(self, value):
        """height setter"""
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if width == 0 or height == 0:
            return 0
        return (2 * (self.__width + self.__height))
