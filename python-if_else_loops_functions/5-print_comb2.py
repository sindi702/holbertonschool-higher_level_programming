#!/usr/bin/python3
for num in range(100):
    formatted_num = "{:02}".format(num)
    if num < 99:
        print(formatted_num, ",", end="")
    else:
        print("{}".format(num))
