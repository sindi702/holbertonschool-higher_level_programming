#!/usr/bin/python3
for num in range(100):
    if num >= 0 & num < 10:
        formatted_num = "{:02}".format(num)
        print(formatted_num, ",", end="")
