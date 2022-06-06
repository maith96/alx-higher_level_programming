#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for l in my_list:
        new_list.append(True if l % 2 == 0 else False)
    return new_list
