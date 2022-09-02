#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    """
    sorted_dict = a_dictionary.copy()
    sorted(sorted_dict.keys())
    for key, value in sorted_dict.items():
        print(key, ":", value)
