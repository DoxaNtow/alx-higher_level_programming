#!/usr/bin/python3
"""defines a function for converting a Python class to a JSON dictionary."""


def class_to_json(obj):
    """Convert a Python class instance to a dictionary representation."""
    return obj.__dict__
