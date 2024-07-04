#!/usr/bin/python3
'''Find the peak value from a list of integers'''
def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
        exit()
    list_of_integers.sort()
    return list_of_integers[-1]
