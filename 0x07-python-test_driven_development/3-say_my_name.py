#!/usr/bin/python3
"""
This module is responsible for printing a person's full name.
"""


def say_my_name(first_name="", last_name=""):
    """
    Display the complete name formed from the provided first name and last name.

    Args:
        first_name (str, optional): The first name.
        last_name (str, optional): The last name. The default is an empty string.

    Raises:
        TypeError: If the first_name is not a string.
        TypeError: If the last_name is not a string.

    Returns:
        None

    """
    # Ensure that first_name and last_name are of the correct type
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    output = ""
    if first_name and last_name:
        output = f"My name is {first_name} {last_name}".strip()
    elif last_name:
        output = f"My name is {last_name}".strip()
    elif first_name:
        output = f"My name is {first_name}".strip()
    else:
        output = "My name is"

    print("{:s}".format(output))
