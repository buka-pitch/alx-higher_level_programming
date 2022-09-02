#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):    """function to multiply each value of a list by some number and return a new list using map"""
    return list(map(lambda x: x * number, my_list))
