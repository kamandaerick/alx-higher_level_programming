#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        counter = 0
        for item in range(x):
            try:
                print("{:d}".format(my_list[item]), end="")
                counter += 1
            except ValueError:
                pass
        print()
        return counter
    except Exception:
        return 0
