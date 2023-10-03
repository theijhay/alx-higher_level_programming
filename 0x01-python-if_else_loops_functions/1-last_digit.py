#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Assign the last digit of the number
num = 0
if number < 0:
    number *= -1
    num = 1

# Get the last digit of the number
lastdig = number % 10

# Check the condition
if num == 1:
    number *= -1
    lastdig *= -1

# Print the last digit of the number
print("Last digit of {:d} is ".format(number), end="")

# Get the greater number
if lastdig > 5:
    # Print the last digit of the number
    print("{:d} and is greater than 5".format(lastdig))

# Print the last digit of the number
elif lastdig == 0:
    print("{:d} and is 0".format(lastdig))
else:
    print("{:d} and is less than 6 and not 0".format(lastdig))
