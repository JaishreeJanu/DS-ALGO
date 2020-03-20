#Problem link: https://www.hackerrank.com/contests/hack-the-interview-u-s-2/challenges/playing-cards-1-1/copy-from/1321956863

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getRoundResult' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. CHARACTER winning_suit
#  2. CHARACTER suit1
#  3. INTEGER number1
#  4. CHARACTER suit2
#  5. INTEGER number2
#

def getRoundResult(winning_suit, suit1, number1, suit2, number2):
    # Write your code here
    if suit1 == winning_suit and suit2 == winning_suit:
        if number1>number2:
            return "Player 1 wins"
        elif number2>number1:
            return "Player 2 wins"
        else:
            return "Draw"
    elif suit1 == winning_suit:
            return "Player 1 wins"
    elif suit2 == winning_suit:
        return "Player 2 wins"
    else:
        if number1>number2:
            return "Player 1 wins"
        elif number2>number1:
            return "Player 2 wins"
        else:
            return "Draw"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    winning_suit = input()[0]

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        suit1 = first_multiple_input[0][0]

        number1 = int(first_multiple_input[1])

        suit2 = first_multiple_input[2][0]

        number2 = int(first_multiple_input[3])

        result = getRoundResult(winning_suit, suit1, number1, suit2, number2)

        fptr.write(result + '\n')

    fptr.close()

