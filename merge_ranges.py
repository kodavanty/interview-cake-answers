#!/usr/bin/python

import sys

'''
'''

def merge_ranges (r):
    # Sort in increasing order of start time.
    r = sorted(r)

    i = 0
    merge_i = 0
    start, end = r[0]
    while i < len(r)-1:
        next_start, next_end = r[i + 1]

        # If next interval is outside current interval add
        if end < next_start:
            r[merge_i] = (start, end)
            merge_i += 1
            i += 1
            start, end = r[i]
            continue

        # If next interval is completely within nothing to be 
        # done continue to the next.
        if next_start < end and next_end <= end:
            i += 1
            continue

        # If overlap extend current end with the next end, the 
        # next intervals end must be greater than current end.
        if next_start <= end:
            end = next_end
            i += 1
            continue

    # Add the last open interval interval
    r[merge_i] = (start, end)

    print r[:merge_i+1]

if __name__ == "__main__":
    r = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    merge_ranges(r)
