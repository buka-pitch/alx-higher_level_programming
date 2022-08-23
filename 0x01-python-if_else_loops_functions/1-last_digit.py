#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Lastnumber = int(str(number)[-1])
if Lastnumber < 6 and Lastnumber != 0:
    print(f"Last digit of {number} is {Lastnumber}\
    and is less than 6 and not 0")
elif Lastnumber > 5:
    print(f"Last digit of {number} is {Lastnumber} and is greater than 5")
elif Lastnumber == 0:
    print(f"Last digit of {number} is {Lastnumber} and is 0")
