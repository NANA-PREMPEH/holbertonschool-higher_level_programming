#!/usr/bin/python3
"""BaseGeometry"""


class BaseGeometry():
    """BaseGeometry"""

    def area(self):
        """Area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
