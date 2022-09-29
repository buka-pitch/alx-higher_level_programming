#!/usr/bin/python3

"""single function to write to a file"""


def write_file(filename="", text=""):
    """function to write text to a specified file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
