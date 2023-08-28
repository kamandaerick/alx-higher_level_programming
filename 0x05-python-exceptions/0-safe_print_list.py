#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for item in my_list:
            if counter < x:
                print(item, end="")
                counter += 1
        print()
        return counter
    except TypeError:
        return 0
    except IndexError:
        return 0
