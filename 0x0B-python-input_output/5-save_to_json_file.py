#!/usr/bin/python3
"""This script defines a function for saving a Python object to a JSON file."""
import json

def save_to_json_file(my_obj, filename):
    """Serialize a Python object to a JSON file.

    Args:
        my_obj: The Python object to be saved in JSON format.
        filename (str): The name of the file to save the JSON data.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
