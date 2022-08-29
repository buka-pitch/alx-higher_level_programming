#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ function to return a new copy of previous list but with some changes"""
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
