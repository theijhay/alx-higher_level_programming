#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        # Return the result of the function.
        result = fct(*args)
        return result
    except Exception as error:
        # print in stderr the error precede by Exception.
        print("Exception: {}".format(error), file=sys.stderr)
        return None
