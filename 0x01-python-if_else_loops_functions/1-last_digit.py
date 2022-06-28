#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if number > 0:
    str_num = str(number)[-1]
    test_num = int(str_num)

elif number < 0:
    str_num = str(number)[-1]
    test_num = int(str_num) * -1

else:
    test_num = 0

if test_num == 0:
    print(f'Last digit of {number} is {test_num} and is 0')

elif test_num < 6 and test_num != 0:
    print(f'Last digit of {number} is {test_num} and is less than 6 and not 0')

elif test_num > 5:
    print(f'Last digit of {number} is {test_num} and is greater than 5')
