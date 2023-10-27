#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    def remove_letter(string, letter):
        new_string = ""
        for char in string:
            if char != letter:
                new_string += char
        return new_string

    if "A" in s:
        transition = remove_letter(s, "A")
        final_result = remove_letter(transition, "M")

        if int(final_result[0] + final_result[1]) == 12:
            final_result = "00" + final_result[2:]

    elif "P" in s:

        transition = remove_letter(s, "P")
        final_result = remove_letter(transition, "M")

        if int(final_result[0] + final_result[1]) == 12:
            return final_result

        start_num = int(final_result[0] + final_result[1])
        final_num = (start_num + 12) % 24
        final_result = str(final_num) + final_result[2:]

    return final_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()