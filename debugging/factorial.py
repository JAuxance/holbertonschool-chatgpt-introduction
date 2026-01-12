#!/usr/bin/env python3

# Holberton code
# ----------------
# import sys

# def factorial(n):
#     result = 1
#     while n > 1:
#         result *= n
#     return result

# f = factorial(int(sys.argv[1]))
# print(f)

#  ./factorial.py 2
# CTraceback (most recent call last):
#   File "/private/tmp/factorial.py", line 9, in 
#     factorial(int(sys.argv[1]))
#   File "/private/tmp/factorial.py", line 5, in factorial
#     while n > 1:

#GPT Correction : 

import sys

def factorial(n):
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <non-negative integer>")
        sys.exit(1)

    n = int(sys.argv[1])
    print(factorial(n))
