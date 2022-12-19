#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return False
    return True
