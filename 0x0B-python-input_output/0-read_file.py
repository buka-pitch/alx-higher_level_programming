#!/usr/bin/python3


def read_file(filename=""):
    """
    function to read files from the filname in the argument
    """
    if filename not None:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
