#!/usr/bin/python3
# Code provided by Holberton School
import sys

def factorial(n):
    """Calculate the factorial of a number recursively."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage:
# This code calculates the factorial of a given number using recursion.
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial_recursive.py <number>")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        print(factorial(num))
    except ValueError:
        print("Please provide a valid integer.")

# Expected output:
# For the command: ./factorial_recursive.py 5
# Output:
# 120