#!/usr/bin/python3
"""defines an object attribute lookup function"""


def lookup(obj):
    """return a list of the available attributes and methods"""
    return (dir(obj))
