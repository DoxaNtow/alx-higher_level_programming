#!/usr/bin/python3

for char_code in range(122, 96, -1):
    if char_code % 2:
        char_code = char_code - 32
    print("{:c}".format(char_code), end="")
