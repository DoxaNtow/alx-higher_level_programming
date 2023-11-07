#!/usr/bin/python3
"""Defines a function for adding attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if it is possible to do so.

    Args:
        obj (any): The object to which an attribute is added.
        att (str): The name of the attribute to be added.
        value (any): The value assigned to the new attribute.
    Raises:
        TypeError: If adding the attribute is not allowed.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add a new attribute to this object.")
    setattr(obj, att, value)
