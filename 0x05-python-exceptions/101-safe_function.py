#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        r = fct(*args)
        return r
    except Exception as err:
        print("Exception: ", err, file=sys.stderr)
        return None

