#!/usr/bin/env python3
def no_c(my_string):
    new_str = [c for c in my_string if c != 'c' and c != 'C']        
    return new_str
