#!/usr/bin/python3
# Code provided by Holberton School
import sys

# Original code:
# This code prints all arguments, including the script name.
# for i in range(len(sys.argv)):
#     print(sys.argv[i])

# Updated code:
# This code prints only the arguments, excluding the script name.
for i in range(1, len(sys.argv)):
    print(sys.argv[i])

# Previous error:
# bash: ./print_arguments.py: Permission denied

# Expected output after fixing the code:
# For the command: ./print_arguments.py 1 2 3
# Output:
# 1
# 2
# 3