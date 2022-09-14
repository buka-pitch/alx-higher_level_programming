
"""
Square class with optional private arg size
"""


class Square:
    """create and helps working with a square
    """

    def __init__(self, size=0):
        if size not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calculates the area of the square
            return the area of the square
        """

        return seld.__size ** 2
