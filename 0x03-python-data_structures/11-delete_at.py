#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """function to delete (remove) specific item on the list using index """
    if idx >= 0 or idx < len(my_list):
        del my_list[idx]
        return my_listi
    else:
        return my_list
