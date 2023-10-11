#!/usr/bin/python3
"""function that adds all unique integers in a list"""


def uniq_add(my_list=[]):
    new_list = set(my_list)
    return sum(new_list)
