#!/usr/bin/python3
def no_c(my_string):
    str_copy = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            str_copy = str_copy + i
    return str_copy
