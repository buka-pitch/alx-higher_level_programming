#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """function to reverse a list and print it each in a new line"""
    if my_list:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
