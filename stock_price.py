#!/usr/bin/python

import sys

'''
'''

def get_max_profit (s):
    l = []
    i = 0
    max_profit = 0
    max_buy = -1
    max_sell = -1
    while i < len(s):
        buy  = -1
        sell = -1
        # Find next low
        while i < len(s)-1 and s[i] >= s[i+1]:
            i += 1
        buy = i

        # Find matching high
        while i < len(s)-1 and s[i] < s[i+1]:
            i += 1
        sell = i

        i += 1
            
        if buy != sell and s[sell]-s[buy] > max_profit:
            max_buy = buy
            max_sell = sell
            max_profit = s[sell]-s[buy]

    print "BUY: %u SELL: %u PROFIT: %u" % (max_buy, max_sell, max_profit)

if __name__ == "__main__":
    stock_prices_yesterday = [10, 7, 5, 8, 11, 9, 5, 6, 9]
    get_max_profit(stock_prices_yesterday)
