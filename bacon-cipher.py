#!/usr/bin/env python3

import sys

alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

n = 5

if len(sys.argv) < 2:
    print("Usage: bacon-cipher.py <encoded string>")
    sys.exit(1)
# TODO: Read from file
# if len(sys.argv) = 3:
# TODO: Read from stdin

encoded = sys.argv[1]

# Strip whitespace
encoded = encoded.replace(" ", "")

# Decode to binary
trans = str.maketrans("AB", "01")
encoded=encoded.translate(trans)

# Group by 5 and lookup in alphabet list
# Python3 so print() is a function and can be used in list comprehensions :)
[print(k, end='') for k in [alphabet[j] for j in [int(result, 2) for result in [encoded[i:i+n] for i in range(0, len(encoded), n)]]]]
# Print newline after decoded message
print()


