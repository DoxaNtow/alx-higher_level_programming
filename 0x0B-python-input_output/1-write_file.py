#!/usr/bin/python3
"""This script defines a function for writing text to files."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): name of the file to write.
        text (str): text to write to file.
    Returns:
        number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
