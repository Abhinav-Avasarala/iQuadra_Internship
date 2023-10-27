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
    total_values = 0
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        total_values += 1
        if i == 0:
            zero += 1
        elif i > 0:
            positive += 1
        else:
            negative += 1
    print(positive / total_values)
    print(negative / total_values)
    print(zero / total_values)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


