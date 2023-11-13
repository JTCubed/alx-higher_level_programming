#!/usr/bin/python3

class Bass:

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id =id
            __nb_objects =+ 1
            id = __nb_objects
