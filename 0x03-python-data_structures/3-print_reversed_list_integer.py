#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # prints all integers of a list, in reverse order.
    if my_list:
        my_list.reverse()
        for abc in my_list:
            print('{:d}'.format(abc))
