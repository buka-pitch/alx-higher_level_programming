#!/usr/bin/python3
"""
Square class with optional private arg size
"""


class Square:
    """create a square object
    """

    def __init__(self, size=None):
        """Initialize the class square
        """

        if size not None:
            self.size = size
