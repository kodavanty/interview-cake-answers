#!/usr/bin/python

import sys

def permutations (s):
    newlists = [[s[0]]]
        
    for c in s[1:]:
        lists = newlists
        newlists = []
        for l in lists:
            # Insert c in each place in the list and create new ones
            for i in range(-1, len(l)):
                newlists.append(l[:i] + [c] + l[i:])

    print newlists

if __name__ == "__main__":
    s = "abc"
    permutations(list(s))
