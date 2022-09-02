#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    function to multiple all the dictionary values by 2
    in a new dictionary
    """
    new_dict = {}
    for i in a_dictionary:
        new_dict[i] = a_dictionary[i] * 2
    return new_dict
