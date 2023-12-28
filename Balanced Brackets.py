import math
import os
import random
import re
import sys


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    stack = []
    dictionary = {')': '(', '}': '{', ']': '['}

    for i in s:
        if i in ['(', '{', '[']:
            stack.append(i)
        elif i in [')', '}', ']']:
            if not stack or dictionary[i] != stack.pop():
                return "NO"

    return "YES" if not stack else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
