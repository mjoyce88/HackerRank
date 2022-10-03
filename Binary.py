#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    b = str(bin(n))[2:]
    p = re.compile(r'1+')
    matches = p.finditer(b)
    result = []
    for m in matches:
        result.append(m.end() - m.start())
        
    print(max(result))
