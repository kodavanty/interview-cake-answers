#!/usr/bin/python

import sys
import random

def rand5 ():
    return random.randint(0, 4)

'''
    Imagine a X, Y grid for 5x5 populated with 0-6 repeated. The last 
    value after the 5th row 1st column is incomplete. So, we will not
    use it.
'''
def rand7 ():

    s = 5*rand5() + rand5()
    while s > 20:
        s = 5*rand5() + rand5()

    return s%7;

if __name__ == "__main__":
    print rand7()
