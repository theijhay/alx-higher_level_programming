#!/usr/bin/python3
for letter in range(97, 123):

    # prints the ASCII alphabet
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")
