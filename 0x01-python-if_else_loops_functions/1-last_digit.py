#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = number % 10

# Print the last digit of the number
print("Last digit of", number, "is", last_digit, end="")

# Print a message depending on the value of the last digit
if last_digit > 5:
    print(" and is greater than 5")

elif last_digit == 0:
    print(" and is 0")

else:
    print(" and is less than 6 and not 0")
