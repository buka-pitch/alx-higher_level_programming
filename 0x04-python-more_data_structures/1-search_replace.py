#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ 
    function to replace specific item of a list
    finding the index of
    the list then replacing the item
    using the index with the new one
    """
    return [replace if i == search else i for i in my_list]
