#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestEvenWord' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def longestEvenWord(sentence):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = longestEvenWord(sentence)

    fptr.write(result + '\n')

    fptr.close()