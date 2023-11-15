#!/usr/bin/python3
"""class that defines square"""


class Square:
    """size is private attribute"""

    def __init__(self , size=0):
        """ initialize a new square.
        args:
            size (int): The size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
