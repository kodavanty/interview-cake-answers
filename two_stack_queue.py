#!/usr/bin/python

import sys

class Queue:
    def __init__(self, size=0):
        self.l1 = []
        self.l2 = []

    # Add to the tail. So, push all elements to the other stack.
    # So that the tail is exposed push element to the stack and
    # push back to the other stack.
    def push (self, val):
        while len(self.l1):
            v = self.l1.pop()
            self.l2.append(v)

        self.l2.append(val)

        while len(self.l2):
            v = self.l2.pop()
            self.l1.append(v)


    # Already in FIFO.
    def pop (self):
        return self.l1.pop()

if __name__ == "__main__":
    s = Queue(10)
    s.push(60)
    s.push(50)
    s.push(40)
    s.push(100)
    print s.pop()
    print s.pop()
    print s.pop()

