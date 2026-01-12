#!/usr/bin/python3
# Code provided by Holberton School
import sys

def factorial(n):
    """Calculate the factorial of a number."""
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Fix: Decrement n to avoid infinite loop
    return result

# Example usage:
# This code calculates the factorial of a given number.
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        print(factorial(num))
    except ValueError:
        print("Please provide a valid integer.")

# Previous error:
# Traceback (most recent call last):
#   File "/private/tmp/factorial.py", line 9, in <module>
#     factorial(int(sys.argv[1]))
#   File "/private/tmp/factorial.py", line 5, in factorial
#     while n > 1:
#           ^^^^^
# KeyboardInterrupt

# Expected output after fixing the code:
# For the command: ./factorial.py 5
# Output:
# 120
