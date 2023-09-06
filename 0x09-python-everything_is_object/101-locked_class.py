#!/usr/bin/python3

"""prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name"""

class LockedClass:
    """prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name"""
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        self.__dict__[name] = value
