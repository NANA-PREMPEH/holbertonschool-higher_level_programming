#!/usr/bin/python3
"""declaration"""


class Square:
    """square"""

    def __init__(self, size=0, position=(0, 0)):
        """size"""
        self.size = size
        self.position = position

    def area(self):
        """area is equal to size**2"""
        return self.__size**2

    def my_print(self):
        """prints square"""
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    @property
    def size(self):
        """returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size to value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position to value"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(n, int) for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if all(n < 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
