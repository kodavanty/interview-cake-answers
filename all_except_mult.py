#!/usr/bin/python

import sys

'''
'''

def all_except (a):

    print a

    left = [1]*len(a)
    right = [1]*len(a)

    for i in range(len(a)):
        left[i] = 1
        right[i] = 1

    left[0] = 1
    right[len(a)-1] = 1

    # All left products
    for i in range(1, len(a)):
        left[i] = a[i-1]*left[i-1]

    # All right products
    for i in range(len(a)-2, -1, -1):
        right[i] = a[i+1]*right[i+1]

    # Product of all other than element
    for i in range(len(a)):
        print left[i]*right[i], 
    print

if __name__ == "__main__":
    all_except([1, 7, 3, 4])
