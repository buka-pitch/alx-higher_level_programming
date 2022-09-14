#!/usr/bin/python3
"""
Square class with optional private arg size
"""


class Square:
    """create a square object
    Args:
        size
    Returns:
        ValueError when size is Negative value
        TypeError when size is not integer

    """

    def __init__(self, size=0):
        """Initialize the class square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
