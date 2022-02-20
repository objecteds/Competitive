#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus = 0
    minus = 0
    zero = 0
    for _ in arr:
        if _ == 0:
            zero += 1
        elif _ > 0:
            plus += 1
        else:
            minus += 1
    
    print(plus/len(arr))
    print(minus/len(arr))
    print(zero/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
