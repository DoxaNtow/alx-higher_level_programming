#!/usr/bin/python3
"""
This script defines a function for looking up object attributes.
"""

def lookup(obj):
    """
    Return a list of all available attributes of an object.
    
    Args:
        obj (object): The object for which attributes will be looked up.
        
    Returns:
        list: A list of available attributes.
    """
    return dir(obj)
