#problem link: https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    N = len(arr)
    #create a map to hold indices of the numbers
    indices_dict = {}
    for i in range(0,N):
        indices_dict[arr[i]] = i
    min_swaps = 0
    for i in range(0,N):
        if arr[i]!=(i+1):
            ind = indices_dict[(i+1)]
            temp = arr[ind]
            arr[ind] = arr[i]
            arr[i] = temp
            indices_dict[arr[i]] = i
            indices_dict[arr[ind]] = ind
            min_swaps += 1
    
    return min_swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

