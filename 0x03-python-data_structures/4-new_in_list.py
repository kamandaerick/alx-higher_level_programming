#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = list(my_list)
    for i in range(len(list_copy)):
        if idx < 0 or idx >= len(list_copy):
            return my_list
        else:
            list_copy[idx] = element
            return list_copy
