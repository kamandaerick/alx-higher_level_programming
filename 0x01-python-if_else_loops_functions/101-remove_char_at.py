#!/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        if i < 0:
            return str
        return str[:n] + str[(n + 1):]
