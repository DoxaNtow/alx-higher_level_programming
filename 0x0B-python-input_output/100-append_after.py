#!/usr/bin/python3
"""This script defines a function for inserting text into a file."""

def append_after(filename="", search_string="", new_string=""):
    """Insert specified text after each line containing a target string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to look for within the file.
    """
    text = ""
    with open(filename) as read_file:
        for line in read_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as write_file:
        write_file.write(text)
