#!/usr/bin/python3
for alpha_lower in range(97, 123):
    if (alpha_lower == 101) or (alpha_lower == 113):
        continue
    print(chr(alpha_lower).format(), end="")
