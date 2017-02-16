#!/usr/bin/python

import sys
import random

def shuffle ():
    l = [i+1 for i in range(52)]
    print l

    for i in range(51):
        j = random.randint(i+1, 51)
        l[i], l[j] = l[j], l[i]

    print l

if __name__ == "__main__":
    shuffle()
