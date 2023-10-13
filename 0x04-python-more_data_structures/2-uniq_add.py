#!/usr/bin/python3

# Add all unique integers in a list (only once for each integer)
def uniq_add(my_list=[]):
    adds = 0
    x = set(my_list)
    for i in x:
        adds += i
    return adds
