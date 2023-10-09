#!/usr/bin/python3
def max_integer(my_list=[]):
    #  find the biggest integer of a list.
    if my_list:
        biggest = my_list[0]
        for i in my_list:
            if i > biggest:
                biggest = i
        return biggest
    else:
        return None
