#!/usr/bin/python3
"""This script defines a function for converting a string to a JSON."""
import json


def to_json_string(my_obj):
    """Convert a string object to its JSON representation.

    Args:
        my_obj: The string object to be converted to JSON.

    Returns:
        A JSON representation of the input string.
    """
    return json.dumps(my_obj)
