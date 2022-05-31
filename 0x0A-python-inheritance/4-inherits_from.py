#!/usr/bin/python3
"""function declaration"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of a class that inherited (directly
    or indirectly) from the specified class"""
    if issubclass(a_class, type(obj)) is False and type(obj) is not a_class:
        return True
    else:
        return False
