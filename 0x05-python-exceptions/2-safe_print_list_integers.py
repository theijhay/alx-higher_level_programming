#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # Assign the value to an integer.
    count = 0
    # Count the number from zero.
    for i in range(0, x):
        # Print the first x elements of a list and only integers.
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
