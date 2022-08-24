#!/usr/bin/python3

def pow(a, b):
    result = 1
    while b:
        result *= a
        b -= 1
    return result
