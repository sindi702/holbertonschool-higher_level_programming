#!/usr/bin/python3
for digit1 in range(10):
    for digit2 in range(digit1, 10):
        if digit1 != digit2:
            number = (digit1 * 10) + digit2
            if (digit1 == 9 and digit2 == 8) or (digit1 == 8 and digit2 == 9):
                print("{:02}".format(number))
            else:
                print("{:02}".format(number), ",", end="")
