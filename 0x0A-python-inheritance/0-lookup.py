#!/usr/bin/python3
"""This script defines a function for looking up object attributes.."""


def lookup(obj):
    """Return a list of all available attributes of an object."""
    return (dir(obj))
