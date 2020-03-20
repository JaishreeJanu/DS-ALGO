#Problem link: https://www.hackerrank.com/contests/hack-the-interview-u-s-2/challenges/heads-or-tails

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxStreaks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY toss as parameter.
#

def getMaxStreaks(toss):
    # Return an array of two integers containing the maximum streak of heads and tails respectively
    heads_max = 0
    tails_max = 0
    i=0
    while i < len(toss):
        heads=0
        tails=0
        while i< len(toss) and toss[i]=='Heads':
            heads += 1
            i+=1
        while i< len(toss) and toss[i]=='Tails':
            tails += 1
            i+=1
        heads_max = max(heads_max,heads)
        tails_max = max(tails_max,tails)
        
    res_arr = [heads_max,tails_max]

    return res_arr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    toss_count = int(input().strip())

    toss = []

    for _ in range(toss_count):
        toss_item = input()
        toss.append(toss_item)

    ans = getMaxStreaks(toss)

    fptr.write(' '.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
