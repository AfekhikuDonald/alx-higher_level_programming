#!/usr/bin/python3
"""creates a function that reads a file and prints to stdout"""


def read_file(filename=""):
    """implement the function"""

    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
