#!/usr/bin/python

import sys
from queue import *

KNIGHT_MOVES = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, 2), (1, 2), (-1, -2), (-1, 2)]

n = 9
visited = {}
path    = {}

def next_move (cur_pos):
    
    c_x, c_y = cur_pos

    for move in KNIGHT_MOVES:
        dx, dy = move

        # If out of bounds check next move
        if c_x + dx < 0 or c_x + dx >= n or c_y + dy < 0 or c_y + dy >= n:
            continue
        
        next_pos = (c_x + dx, c_y + dy)
        yield next_pos

    yield None

def print_path (end):
    p = []
    while end != (-1, -1):
        p.append(end)
        end = path[end]

    print p

def knight_move (n, start, end):

    print n, start, end
    q = Queue()

    # Add start node to path
    q.enqueue(start)

    visited[start] = 1
    path[start] = (-1, -1)

    while not q.isEmpty():
        cur_pos = q.dequeue()
        for next_pos in next_move(cur_pos):
            if next_pos and not next_pos in visited:
                q.enqueue(next_pos)

                visited[next_pos] = 1
                path[next_pos] = cur_pos

                if next_pos == end:
                    print_path(next_pos)
                    return

    print "NO PATH FOUND"

if __name__ == "__main__":
    knight_move(n, (1,1), (1,2))
