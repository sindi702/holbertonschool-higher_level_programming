#!/usr/bin/python3
for num in range(10):
    for digit in range(num + 1, 10):
        print("{:02d}".format(num), "{:02d}".format(digit), end=", ")
print()
