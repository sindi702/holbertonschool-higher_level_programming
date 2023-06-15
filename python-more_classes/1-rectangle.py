#!/usr/bin/python3
'''new class'''


class Rectangle:
    '''init fun'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        self.__height

    @property
    def width(self):
        '''width'''
        self.__width

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
