#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    new_list = arr[:]

    min_values = []
    min_total = 0

    max_values = []
    max_total = 0

    while len(arr) != 0 and len(min_values) < 4:
        min_val = arr[0]
        for i in arr:
            if i < min_val:
                min_val = i
        min_values.append(min_val)
        arr.remove(min_val)

    while len(new_list) != 0 and len(max_values) < 4:
        max_val = new_list[0]
        for j in new_list:
            if j > max_val:
                max_val = j
        max_values.append(max_val)
        new_list.remove(max_val)

    for i in range(4):
        min_total += min_values[i]
        max_total += max_values[i]

    print(f"{min_total} {max_total}")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
