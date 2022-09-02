#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """delete a dict with a key"""
    if key in a_dictionary:
        a_dictionary.__delitem__(key)
    return a_dictionary
