#!/usr/bin/python3
"""Defines same class or inherit from."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class."""
    if isinstance(obj, a_class):
        return True
    return False
