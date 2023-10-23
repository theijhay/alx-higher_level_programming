#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # Assign the new list to an empty array.
    new_list = []
    # returns a sequence of numbers from 0 to the specified length.
    for i in range(list_length):
        try:
            # Returns a new list (length = list_length) with all divisions.
            result = my_list_1[i] / my_list_2[i]
            # If an element is not an integer or float.
        except TypeError:
            print("wrong type")
            result = 0
            # If the division can’t be done (/0):
        except ZeroDivisionError:
            print("division by 0")
            result = 0
            # If my_list_1 or my_list_2 is too short.
        except IndexError:
            print("out of range")
            result = 0
            # Add the result on the finally.
        finally:
            new_list.append(result)
    return new_list
