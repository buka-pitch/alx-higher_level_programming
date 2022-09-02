#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ function to replace specific item of a list 
        by copying the list and finding the index of
        the list then replacing the item
        using the index with the new one
    """
    new_list = my_list.copy()
    i = my_list.index(search)
    new_list[i] = replace
    return new_list



