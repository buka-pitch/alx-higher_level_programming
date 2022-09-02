#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    function to sort a dict by order
    """
    for i in sorted(a_dictionary):
        print('{} : {}'.format(i, a_dictionary[i]))
