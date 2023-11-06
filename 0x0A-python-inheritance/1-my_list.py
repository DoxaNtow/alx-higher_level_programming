#!/usr/bin/python3
"""Defines an inherited list class called  MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print the list in sorted ascending order."""
        print(sorted(self))
