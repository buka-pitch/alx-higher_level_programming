#!/usr/bin/python3
def no_c(my_string):
    """function to remove 'c' and 'C' charachters from any text"""
    new_str = my_string.translate({ord(i): None for i in 'cC'})    
    return new_str
