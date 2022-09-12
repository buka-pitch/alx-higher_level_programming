#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    function to print x amount of the list in a safe way
    """
    if x == 0:
        return 0
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
    except IndexError:
        return i
    return i + 1
