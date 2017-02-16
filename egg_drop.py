#!/usr/bin/python

import sys

'''
    Cases are egg breaks or doesn't break on a given floor. 
    If egg breaks we need to check the rest of the floors below with minus one egg.
    If egg doesn't break we need to check the floors above with the same number of 
    eggs.
    Since we need to consider the worst case, we take the max of the two cases above.
    But, we also need to check these two cases for all floors from 1 to n and get the 
    minimum. And finally we account for the 1 try we will waste for this floor.

    MIN_TRY[m][n] = 1 + min(max{MIN_TRY[m-1][n-1], MIN_TRY[m][n-i]} i going from 1 to n)
'''

def egg_drop (m, n):
    print "EGGS %u FLOORS %u" % (m, n)

    MIN_TRY = [[0 for i in range(n+1)] for j in range(m+1)]

    # N eggs on 0 and 1 floor need 0 and 1 tries.
    for i in range(m+1):
        MIN_TRY[i][0] = 0
        MIN_TRY[i][1] = 1

    # 1 egg N floors needs N tries starting at the top floor. For 0 eggs 0
    for i in range(n+1):
        MIN_TRY[0][i] = 0
        MIN_TRY[1][i] = i

    for egg in range(2, m+1):
        for floor in range(2, n+1):
            MIN_TRY[egg][floor] = sys.maxint
            for j in range(1, floor+1):
                # For a given floor worst case of egg breaking and not breaking
                maximum = 1 + max(MIN_TRY[egg-1][j-1], MIN_TRY[egg][floor-j])
                # Minimum across all floors till floor
                MIN_TRY[egg][floor] = min(MIN_TRY[egg][floor], maximum)

    print MIN_TRY[m][n]

if __name__ == "__main__":
    egg_drop(2, 100)
