#!/usr/bin/python

import sys

def reverse_str (s):
    l = [c for c in s]
    le = len(l)

    for i in range(le/2):
        l[i], l[le-i-1] = l[le-i-1], l[i]

    print l

if __name__ == "__main__":
    reverse_str("vamsikodavanty")
