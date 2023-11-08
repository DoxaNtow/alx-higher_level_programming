#!/usr/bin/python3
# 6-from_json_string.py
"""Script defines a function for converting  JSON string to  Python object."""
import json


def from_json_string(my_str):
    """Convert a JSON string into its corresponding Python object.

    Args:
        my_str (str): A JSON-formatted string.

    Returns:
        The Python object representation of the input JSON string.
    """
    return json.loads(my_str)
