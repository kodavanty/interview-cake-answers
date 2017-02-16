#!/usr/bin/python

import sys

'''
    Maximum of values including and excluding item.
    V[item][wt] =
        MAX (v[item] + V[item-1][wt - W[item]] if wt-W[item] > 0,
             V[item-1][wt])
'''

def knapsack (weight, items):
    V = [[0 for w in range(weight+1)] for i in range(len(items)+1)]

    for i in range(1, len(items)+1):
        item_wt, item_val = items[i-1]
        for w in range(1, weight+1):
            include = 0
            if item_wt <= w:
                include = item_val + V[i-1][w-item_wt]
            exclude = V[i-1][w]
            V[i][w] = max(include, exclude)

    print V[len(items)][weight]

'''
    Maximum of include 1 or multiple items of a kind and excluding the item

    V[item][wt] = MAX({i=0 to n while i*W[item] < WEIGHT V[item][wt-i*W[item]]},
                       V[item-1][wt])
'''
def knapsack_unlimited (weight, items):
    V = [[0 for w in range(weight+1)] for i in range(len(items)+1)]

    for i in range(1, len(items)+1):
        item_wt, item_val = items[i-1]
        for w in range(1, weight+1):
            # Calculate the max of including one or more items
            j = 1
            max_include = 0
            while (j*item_wt <= w):
                include = j*item_val + V[i-1][w - j*item_wt]                
                max_include = max(include, max_include)
                j += 1
            exclude = V[i-1][w]

            V[i][w] = max(max_include, exclude)

    print V[len(items)][weight]

if __name__ == "__main__":
    #knapsack(60, [(10, 60), (20, 100), (30, 120)])
    knapsack_unlimited(70, [(50, 60), (20, 300), (10, 100)])
