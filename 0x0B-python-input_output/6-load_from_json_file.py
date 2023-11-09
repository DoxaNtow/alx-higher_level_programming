#!/usr/bin/python3
"""defines a function for reading a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """Deserialize a Python object from a JSON f """
    with open(filename) as file:
        return json.load(file)
