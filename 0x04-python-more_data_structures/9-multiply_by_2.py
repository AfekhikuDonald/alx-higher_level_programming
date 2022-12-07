#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dicttionary.copy()
    for i in new_dict.keys():
        i *= 2
    return (new_dict)
