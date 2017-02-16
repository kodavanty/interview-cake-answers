#!/usr/bin/python

import sys
from queue import *

class Stack:
    def __init__(self, size=0):
        self.q1 = Queue()
        self.q2 = Queue()

    '''
        Enqueue in an empty queue and enqueue other on top
    '''
    def push (self, val):
        pushq, popq = (self.q2, self.q1) if self.q2.isEmpty() else (self.q1, self.q2)

        pushq.enqueue(val) 
        while not popq.isEmpty():
            v = popq.dequeue()
            pushq.enqueue(v)

    '''
        Dequeue from the populated queue.
    '''
    def pop (self):
        popq = self.q2 if self.q1.isEmpty() else self.q1
        return popq.dequeue()

if __name__ == "__main__":
    s = Stack()
    s.push(50)
    s.push(40)
    s.push(100)
    print s.pop()
    print s.pop()
    print s.pop()

