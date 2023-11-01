#!/usr/bin/python3
"""LockedClass Definition"""

class LockedClass:
    """
    This class prevents the creation of new attributes except for 'first_name'.
    """
    __slots__ = ["first_name"]
