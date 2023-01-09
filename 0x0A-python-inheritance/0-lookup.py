#!/usr/bin/python3

def lookup(obj):
    object_methods = [method_name for method_name in dir(object)
                  if callable(getattr(object, method_name))]
    return (object_methods)
