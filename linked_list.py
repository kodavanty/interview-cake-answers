#!/usr/bin/python

import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None

def print_list (n):
    while n:
        print n.value,
        n = n.next

    print

def reverse_recursive (l):
    if not l.next:
        return (l, l)

    nxt, root = reverse_recursive(l.next)
    nxt.next = l
    l.next = None

    return (l, root)

def reverse (l):
    prev = None
    cur  = l
    nxt = cur

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev
        
def kth_to_last (l, k):
    runner = l

    n = k
    while n and runner:
        runner = runner.next
        n -= 1

    if n:
        print "LIST < K nodes"
        return

    kptr = l
    while runner:
        kptr = kptr.next
        runner = runner.next

    print "KTH VALUE :" + str(kptr.value)

if __name__ == "__main__":
    l = Node(2)
    l.next = Node(5)
    l.next.next = Node(6)
    l.next.next.next = Node(9)
    l.next.next.next.next = Node(12)

    print_list(l)
    kth_to_last(l, 1)

    '''
    r, h = reverse_recursive(l)
    print_list(h)
    '''
