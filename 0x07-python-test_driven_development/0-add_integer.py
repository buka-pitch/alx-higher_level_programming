#!/usr/bin/python3

def add_integer(a, b=98):
    """ function to add and return the additions of two numbers
    """
    if a == None:
        raise SyntaxError("add a number to add")
    elif not isinstance(a, (int, float)):
        raise TypeError("a must be integer")
    elif isinstance(a, float):
        a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be integer")

    #returns the addition of a and b
    return int(a) + int(b)

