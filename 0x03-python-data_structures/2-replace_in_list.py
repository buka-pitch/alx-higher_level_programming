#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """function to replace a specific item on a given list"""

    if idx < 0 or idx > len(my_list):
        return my_list

    new_list = my_list
    new_list[idx] = element
    return new_list
