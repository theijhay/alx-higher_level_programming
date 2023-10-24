#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    # Print the integer.
    try:
        print("{:d}".format(value))
        # Returns True if value has been correctly printed.
        return True
    # Return False and prints in stderr the error precede by Exception:
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
