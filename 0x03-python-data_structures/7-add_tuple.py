#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    arg_a1, arg_a2, arg_b1, arg_b2 = 0, 0, 0, 0
    if len(tuple_a) == 1:
        arg_a1 = tuple_a[0]
    elif len(tuple_a) > 1:
        arg_a1, arg_a2 = tuple_a[0], tuple_a[1]
    if len(tuple_b) == 1:
        arg_b1 = tuple_b[0]
    elif len(tuple_b) > 0:
        arg_b1, arg_b2 = tuple_b[0], tuple_b[1]
    new_tuple = arg_a1 + arg_b1, arg_a2 + arg_b2
    return new_tuple
