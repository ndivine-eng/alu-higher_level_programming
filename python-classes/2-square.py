#!/usr/bin/python3
"""class that defines square"""


class Square:
    """size is private attribute"""
    def __init__(self , size=0):
        """
        args:
            size (int): New size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an intiger")
        elif size < 0:
            raise ValueError("size must be >= o")
        self.__size = size
