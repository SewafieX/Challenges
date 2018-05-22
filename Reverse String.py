from math import pi
import sys
import datetime


def reverse(string):
    return string[::-1]


name = input("Your name is: ")
rev = reverse(name)
print(rev)
