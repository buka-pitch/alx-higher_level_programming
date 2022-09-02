#!/usr/bin/python3
def best_score(a_dictionary):
    """
        function to get the max number from the dictionary 
        value and return the key
    """
    if a_dictionary == None:
        return None
    return max(a_dictionary.items())
