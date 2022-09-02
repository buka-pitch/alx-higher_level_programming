#!/usr/bin/python3
def best_score(a_dictionary):
    """
    function to get the max number from the dictionary
    value and return the key
    """
    if a_dictionary is None or a_dictionary == {}:
        return None
    res = max(a_dictionary.items(), key=lambda n: n[1])[0]
    return res
