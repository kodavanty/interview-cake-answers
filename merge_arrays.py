#!/usr/bin/python

import sys

'''
'''

def merge_arrays (a, b):
    m = []
    i1 = i2 = 0

    while i1 < len(a) or i2 < len(b):
        if i1 == len(a):
            m.append(b[i2])
            i2 += 1
        elif i2 == len(b):
            m.append(a[i1])
            i1 += 1
        elif a[i1] < b[i2]:
            m.append(a[i1])
            i1 += 1
        else:
            m.append(b[i2])
            i2 += 1

    print m

if __name__ == "__main__":
    merge_arrays([1, 5, 10, 11, 15, 25, 40], [0, 20, 30, 34, 50])
