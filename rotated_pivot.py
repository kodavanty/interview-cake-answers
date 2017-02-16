#!/usr/bin/python

import sys

def rotated_pivot (a):

    lo = 0
    hi = len(a)-1

    while lo <= hi:
        mid = lo + (hi-lo)/2

        # Check if we found the pivot
        if mid > lo and a[mid-1] > a[mid]: 
            print "PIVOT: " + str(mid-1)
            return
        if mid < hi and a[mid] > a[mid+1]:
            print "PIVOT: " + str(mid)
            return

        # Check if pivot in the left or right half
        if a[mid] < a[lo]:
            # Pivot in left half
            hi = mid - 1
        else:
            # Pivot in right half
            lo = mid + 1

if __name__ == "__main__":
    rotated_pivot([5, 6, 7, 1, 2, 3, 4])
