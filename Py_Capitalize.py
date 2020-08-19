#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.

def main():
    solve(s)

def solve(s):
    a = s.split()
    b = a[0]
    c = a[1]
    return re.sub(' 3G',' 3G'.lower(),s.title())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
