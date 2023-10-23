#!/usr/bin/python3
def safe_print_division(a, b):
    # The result of dividing a by b, or None if b is 0.
    try:
        result = a / b
    except ZeroDivisionError:
        # Assign the result to None.
        result = None
        # Print the result of the division on the finally.
    finally:
        print("Inside result: {}".format(result))
        # Return the result.
    return result
