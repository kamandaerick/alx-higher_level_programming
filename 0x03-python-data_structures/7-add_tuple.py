#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuplea_copy = tuple_a + (0, 0)
    tupleb_copy = tuple_b + (0, 0)
    sum1 = tuplea_copy[0] + tupleb_copy[0]
    sum2 = tuplea_copy[1] + tupleb_copy[1]
    return (sum1, sum2)
