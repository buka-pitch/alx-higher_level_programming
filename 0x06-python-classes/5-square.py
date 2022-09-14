#!/usr/bin/python3
"""
Square class
"""


class Square:
    """create and helps working with a square
    """

    def __init__(self, size=0):
        """initialize the square class
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calculates the area of the square
            return the area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the value of the square size to the 'value'
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the squares
            prints empty if size is 0
        """

        if self.size == 0:
            return print()
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
