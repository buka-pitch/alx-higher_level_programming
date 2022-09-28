#!/usr/bin/python3


def read_file(filename=""):
    if filename not None:
        with open(filename, 'r') as f:
            print(f.read())
