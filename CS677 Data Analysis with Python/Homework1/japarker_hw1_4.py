# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: March 18, 2022
Homework Problem 1.4

Simulate the "oracle driven" trading strategy for PFE and SPY.
For either stock, starting with $100, make optimal trades knowing
if the adjusted closing price the next day will be a gain or a loss.
"""
import os
import operator

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW1')

# Import helper functions to stock data from file.
from JparkerHw1Helper import *

# Get the PFE list and sort it by date.
pfe_list = JparkerHw1Helper.load_ticker('PFE')
pfe_list = sorted(pfe_list, key=operator.itemgetter(0))

# The trading oracle provides insight into the days adjusted closing price.
# If the price will close up, sell.
# If the price will go down, buy.
# Keep track of shares held and cash on hand.

pfe_cash = 100
pfe_shares = 0
for i in range(0, len(pfe_list)):

    # First day, must buy... if there is money.
    if i == 0 and pfe_cash >= pfe_list[i][3]:
#       print ("Initial buy " + " ".join(map(str, pfe_list[i])))
#       print ("Initital buy", end = '')
        pfe_shares = pfe_cash // pfe_list[i][3]
        pfe_cash = pfe_cash - round((pfe_shares * pfe_list[i][3]), 2)

    # If the price is up, sell, if there is something to sell.
    elif pfe_list[i][4] > 0 and pfe_shares > 0:
#       print ("SELL! " + " ".join(map(str, pfe_list[i])))
#       print ("SELL!\t", end = '')
        pfe_cash = pfe_cash + round((pfe_shares * pfe_list[i][3]), 2)
        pfe_shares = 0

    # If the price is down, buy, if there is enough money to buy.
    elif pfe_list[i][4] < 0 and pfe_cash >= pfe_list[i][3]:
#       print ("BUY! " + " ".join(map(str, pfe_list[i])))
#       print ("BUY!\t", end = '')
        pfe_shares += pfe_cash // pfe_list[i][3]
        pfe_cash = pfe_cash - round(((pfe_cash // pfe_list[i][3]) * pfe_list[i][3]), 2)

    # If nothing else, hold.
    else:
#       print ("hold " + " ".join(map(str, pfe_list[i])))
#       print ("hold\t", end = '')
        pass

    # How are we doing?
#   print(pfe_list[i][0] + "\t${:,.2f}\t{:.0f}".format(pfe_cash, pfe_shares))
# End for pfe_trading.

# Sell any remaining shares for cash.
pfe_cash = pfe_cash + round((pfe_shares * pfe_list[i][3]), 2)
pfe_shares = 0
print("Pfizer Final:\t${:,.2f}".format(pfe_cash))


##### DO IT AGAIN FOR SPY! #####
# Comments and test printing removed.
spy_list = JparkerHw1Helper.load_ticker('SPY')
spy_list = sorted(spy_list, key=operator.itemgetter(0))

spy_cash = 100
spy_shares = 0
for i in range(0, len(spy_list)):
    if i == 0 and spy_cash >= spy_list[i][3]:
        spy_shares = spy_cash // spy_list[i][3]
        spy_cash = spy_cash - round((spy_shares * spy_list[i][3]), 2)

    elif spy_list[i][4] > 0 and spy_shares > 0:
        spy_cash = spy_cash + round((spy_shares * spy_list[i][3]), 2)
        spy_shares = 0

    elif spy_list[i][4] < 0 and spy_cash >= spy_list[i][3]:
        spy_shares += spy_cash // spy_list[i][3]
        spy_cash = spy_cash - round(((spy_cash // spy_list[i][3]) * spy_list[i][3]), 2)

    else:
        pass
# End for spy_trading.

# Sell any remaining shares for cash.
spy_cash = spy_cash + round((spy_shares * spy_list[i][3]), 2)
spy_shares = 0
print("S&P 500 Final:\t${:,.2f}".format(spy_cash))
