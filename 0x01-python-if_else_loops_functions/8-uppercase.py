#!/usr/bin/python3
def uppercase(str):
    buf = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            buf += chr(ord(i) - 32)
        else:
            buf += i
    print("{}".format(buf))
