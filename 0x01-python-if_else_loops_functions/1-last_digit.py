#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_val = 0
if number < 0:
    number *= -1
    abs_val = 1
last_digit = number % 10
if abs_val == 1:
    number *= -1
    last_digit *= -1
print("Last digit of {:d} is ".format(number), end="")
if last_digit > 5:
    print("{} and is greater than 5".format(last_digit))
elif last_digit == 0:
    print("{} and is 0".format(last_digit))
elif last_digit < 6 and last_digit != 0:
    print("{} and is less than 6 and not 0".format(last_digit))