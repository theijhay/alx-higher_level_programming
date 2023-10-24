#!/usr/bin/python3
def magic_calculation(a, b):
    # Assign the value to the integer.
    result = 0
    # returns a sequence of numbers from 0 to the specified length.
    for i in range(1, 3):
        try:
            # Check which one is greater or lesser.
            if i > a:
                # Raise the exception not too far.
                raise Exception('Too far')
            else:
                result += a ** b / i
        except:
            result = b + a
            break
    return (result)
