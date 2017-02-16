#!/usr/bin/python

import sys

OPEN_BRACES = ['{', '(', '[']
CLOSE_BRACES = ['}', ')', ']']

def match_paranthesis (s, pos):
    stack = []

    for i,c in enumerate(s):
        if not c in OPEN_BRACES and not c in CLOSE_BRACES:
            continue

        if c in OPEN_BRACES:
            stack.append((i, c))
        else:
            idx = CLOSE_BRACES.index(c)
            oi, oc = stack[len(stack)-1]
            if oc == OPEN_BRACES[idx]:
                if oi == pos:
                    print "FOUND MATCHING CLOSE %u:%u %c:%c" % (oi, i, s[oi], s[i])
                    return
                stack.pop()

    if len(stack):
        print "BRACES NOT MATCHING"

if __name__ == "__main__":
    match_paranthesis("Sometimes (when I nest them (my parentheticals ) too much (like this (and this))) they get confusing.", 10)
