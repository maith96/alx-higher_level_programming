#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = -98
print(f'Last digit of {number} is {number % 10} and ', end='')
number %= 10
if number > 5:
    print('is greater than 5')
if number == 0:
    print('is 0')
if number < 6:
    print('is less than 6 and not 0')
