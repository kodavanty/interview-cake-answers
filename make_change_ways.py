#!/usr/bin/python

import sys

'''
'''

def make_change_ways (val, denom):
    w = [[0 for c in range(val+1)] for r in range(len(denom))]

    # For v = 0 there is only 1 way to make change.
    for r in range(len(denom)):
        w[r][0] = 1

    for di, d in enumerate(denom):
        for v in range(1, val+1):
        
            # If v < d there is only 1 way to make change.
            # Check with a lower denomination.
            if v < d:
                w[di][v] = w[di-1][v]
            else:
                w[di][v] = w[di-1][v] + w[di][v-d]

    print w[len(denom)-1][val]

if __name__ == "__main__":
    make_change_ways(5, [1,2,3])


