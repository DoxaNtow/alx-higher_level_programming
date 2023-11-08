#!/usr/bin/python3
"""This script provides a function for reading text files."""


def read_file(filename=""):
    """
    Display the contents of a UTF-8 encoded text file on the standard output.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
