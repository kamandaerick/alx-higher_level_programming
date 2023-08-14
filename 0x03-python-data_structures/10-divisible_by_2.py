#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for i in my_list:
        is_even = i % 2 == 0
        result.append(is_even)

    return result
