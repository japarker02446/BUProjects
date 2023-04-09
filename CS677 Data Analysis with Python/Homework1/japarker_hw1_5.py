# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: March 18, 2022
Homework Problem 1.5

Simulate the "buy and hold" trading strategy for PFE and SPY.
For either stock, starting with $100, buy on the first day and sell on the
last day.
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

pfe_cash = 100
pfe_shares = 0

# Buy on day 1.
if pfe_cash >= pfe_list[0][3]:
    pfe_shares = pfe_cash // pfe_list[0][3]
    pfe_cash = pfe_cash - round((pfe_shares * pfe_list[0][3]), 2)

# Sell on day last.
pfe_cash = pfe_cash + round((pfe_shares * pfe_list[-1][3]), 2)
pfe_shares = 0
print("Pfizer Final:\t${:,.2f}".format(pfe_cash))

##### DO IT AGAIN FOR SPY! #####
spy_list = JparkerHw1Helper.load_ticker('SPY')
spy_list = sorted(spy_list, key=operator.itemgetter(0))

spy_cash = 100
spy_shares = 0

# Buy on day 1.
if spy_cash >= spy_list[0][3]:
    spy_shares = spy_cash // spy_list[0][3]
    spy_cash = spy_cash - round((spy_shares * spy_list[0][3]), 2)

# Sell on day last.
spy_cash = spy_cash + round((spy_shares * spy_list[-1][3]), 2)
spy_shares = 0
print("S&P 500 Final:\t${:,.2f}".format(spy_cash))

# duh, of course SPY is unchanged.  Shares cost more than $100.
