#!/usr/bin/python3

def no_c(my_string):
    """Remove 'c' and 'C' characters from a string."""
    new_string = "".join([char for char in my_string if char not in 'cC'])
    return new_string
