#!/usr/bin/python3
def pow(a, b):
    c=a
    for i in range(1, b):
        c *= a
    return c
