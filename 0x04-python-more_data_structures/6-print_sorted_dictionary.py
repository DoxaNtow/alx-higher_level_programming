#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = sorted(a_dictionary)
    for key in list_ord:
        print("{}: {}".format(key, a_dictionary[key]))
