#!/bin/python3

import math
import os
import random
import re
import sys


def factorial(n):
    fact_memo = {}

# exit condition is when n <= 1
    if n <=1: return 1

# recursive rule is f(n) = n * f(n-1)
    if n in fact_memo.keys(): return n * fact_memo[n]
    else:
        memo = factorial(n-1)
        fact_memo[n] = memo
    return n * memo    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
