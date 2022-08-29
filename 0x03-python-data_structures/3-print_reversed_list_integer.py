#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """function to reverse a list and print it each in a new line"""

    my_list.reverse()
    for i in my_list:
        print("{}".format(i), end='\n')

