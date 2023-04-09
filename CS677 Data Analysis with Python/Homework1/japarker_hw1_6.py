# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: March 18, 2022
Homework Problem 1.6

Simulate the "oracle angry" trading strategy for PFE and SPY.
For either stock, starting with $100, make optimal trades knowing
if the adjusted closing price the next day will be a gain or a loss.

For part A, miss the best 10 trading days and your profit is lower.  My
understanding is that you DO NOT SELL on the top 10 GAIN DAYS.
For part B, realize the worst 10 trading days.  My understanding is you DO
SELL on the bottom 10 (lowest) LOSS DAYS.
For part C, you miss the top 5 and realize the worst 5 trading days.

Run all three for both PFE and SPY.
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

# Get the PFE list.
pfe_list = JparkerHw1Helper.load_ticker('PFE')

# Sort the PFE list by the percent gain to identify the top and bottom five
# or 10 days.
pfe_list = sorted(pfe_list, key=operator.itemgetter(4))
pfe_top10 = pfe_list[0:10]
pfe_top5 = pfe_list[0:5]
pfe_bottom10 = pfe_list[-10:]
pfe_bottom5 = pfe_list[-5:]

# Sort the PFE list by date to commence trading.
pfe_list = sorted(pfe_list, key=operator.itemgetter(0))

#####
# PART A - Miss the top 10 Trading days / DO NOT SELL on Top 10 Days.
# The trading oracle provides insight into the days adjusted closing price.
# If the price will close up, sell.
# If the price will go down, buy.
# Keep track of shares held and cash on hand.
pfe_cash = 100
pfe_shares = 0
for i in range(0, len(pfe_list)):

    # First day, must buy... if there is money.
    if i == 0 and pfe_cash >= pfe_list[i][3]:
        pfe_shares = pfe_cash // pfe_list[i][3]
        pfe_cash = pfe_cash - round((pfe_shares * pfe_list[i][3]), 2)

    # Don't sell on the best days.
    elif pfe_list[i] in pfe_top10:
        next

    # If the price is up, sell, if there is something to sell.
    elif pfe_list[i][4] > 0 and pfe_shares > 0:
        pfe_cash = pfe_cash + round((pfe_shares * pfe_list[i][3]), 2)
        pfe_shares = 0

    # If the price is down, buy, if there is enough money to buy.
    elif pfe_list[i][4] < 0 and pfe_cash >= pfe_list[i][3]:
        pfe_shares += pfe_cash // pfe_list[i][3]
        pfe_cash = pfe_cash - round(((pfe_cash // pfe_list[i][3]) * pfe_list[i][3]), 2)

    # If nothing else, hold.
    else:
        pass
# End for pfe_trading.

# Sell any remaining shares for cash.
pfe_cash = pfe_cash + round((pfe_shares * pfe_list[i][3]), 2)
pfe_shares = 0
print("Pfizer Part A Final:\t${:,.2f}".format(pfe_cash))

##### DO IT AGAIN FOR SPY! #####
# This is kind of a moot exercise since $100 isn't enough to buy a single share.
# Comments and test printing removed.
spy_list = JparkerHw1Helper.load_ticker('SPY')

spy_list = sorted(spy_list, key=operator.itemgetter(4))
spy_top10 = spy_list[0:10]
spy_top5 = spy_list[0:5]
spy_bottom10 = spy_list[-10:]
spy_bottom5 = spy_list[-5:]

spy_list = sorted(spy_list, key=operator.itemgetter(0))
spy_cash = 100
spy_shares = 0
for i in range(0, len(spy_list)):
    if i == 0 and spy_cash >= spy_list[i][3]:
        spy_shares = spy_cash // spy_list[i][3]
        spy_cash = spy_cash - round((spy_shares * spy_list[i][3]), 2)

    elif spy_list[i] in spy_top10:
        next

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
print("S&P 500 Part A Final:\t${:,.2f}".format(spy_cash))

#####
# PART B - realize the worst 10 trading days / SELL ON THE 10 WORST LOSS DAYS.
pfe_cash = 100
pfe_shares = 0
for i in range(0, len(pfe_list)):

    # First day, must buy... if there is money.
    if i == 0 and pfe_cash >= pfe_list[i][3]:
        pfe_shares = pfe_cash // pfe_list[i][3]
        pfe_cash = pfe_cash - round((pfe_shares * pfe_list[i][3]), 2)

    # Sell on the worst down days.
    elif pfe_list[i] in pfe_bottom10:
        pfe_cash = pfe_cash + round((pfe_shares * pfe_list[i][3]), 2)
        pfe_shares = 0

    # If the price is up, sell, if there is something to sell.
    elif pfe_list[i][4] > 0 and pfe_shares > 0:
        pfe_cash = pfe_cash + round((pfe_shares * pfe_list[i][3]), 2)
        pfe_shares = 0

    # If the price is down, buy, if there is enough money to buy.
    elif pfe_list[i][4] < 0 and pfe_cash >= pfe_list[i][3]:
        pfe_shares += pfe_cash // pfe_list[i][3]
        pfe_cash = pfe_cash - round(((pfe_cash // pfe_list[i][3]) * pfe_list[i][3]), 2)

    # If nothing else, hold.
    else:
        pass
# End for pfe_trading.

# Sell any remaining shares for cash.
pfe_cash = pfe_cash + round((pfe_shares * pfe_list[i][3]), 2)
pfe_shares = 0
print("Pfizer Part B Final:\t${:,.2f}".format(pfe_cash))

###### PART B for SPY
spy_cash = 100
spy_shares = 0
for i in range(0, len(spy_list)):

    # First day, must buy... if there is money.
    if i == 0 and spy_cash >= spy_list[i][3]:
        spy_shares = spy_cash // spy_list[i][3]
        spy_cash = spy_cash - round((spy_shares * spy_list[i][3]), 2)

    # Sell on the worst down days.
    elif spy_list[i] in spy_bottom10:
        spy_cash = spy_cash + round((spy_shares * spy_list[i][3]), 2)
        spy_shares = 0

    # If the price is up, sell, if there is something to sell.
    elif spy_list[i][4] > 0 and spy_shares > 0:
        spy_cash = spy_cash + round((spy_shares * spy_list[i][3]), 2)
        spy_shares = 0

    # If the price is down, buy, if there is enough money to buy.
    elif spy_list[i][4] < 0 and spy_cash >= spy_list[i][3]:
        spy_shares += spy_cash // spy_list[i][3]
        spy_cash = spy_cash - round(((spy_cash // spy_list[i][3]) * spy_list[i][3]), 2)

    # If nothing else, hold.
    else:
        pass
# End for spy_trading.

# Sell any remaining shares for cash.
spy_cash = spy_cash + round((spy_shares * spy_list[i][3]), 2)
spy_shares = 0
print("S&P 500 Part B Final:\t${:,.2f}".format(spy_cash))

#####
# Part C, miss the top 5 and realize the bottom 5 trading days.
pfe_cash = 100
pfe_shares = 0
for i in range(0, len(pfe_list)):

    # First day, must buy... if there is money.
    if i == 0 and pfe_cash >= pfe_list[i][3]:
        pfe_shares = pfe_cash // pfe_list[i][3]
        pfe_cash = pfe_cash - round((pfe_shares * pfe_list[i][3]), 2)

    # Don't sell on the best days.
    elif pfe_list[i] in pfe_top5:
        next

    # Sell on the worst down days.
    elif pfe_list[i] in pfe_bottom5:
        pfe_cash = pfe_cash + round((pfe_shares * pfe_list[i][3]), 2)
        pfe_shares = 0

    # If the price is up, sell, if there is something to sell.
    elif pfe_list[i][4] > 0 and pfe_shares > 0:
        pfe_cash = pfe_cash + round((pfe_shares * pfe_list[i][3]), 2)
        pfe_shares = 0

    # If the price is down, buy, if there is enough money to buy.
    elif pfe_list[i][4] < 0 and pfe_cash >= pfe_list[i][3]:
        pfe_shares += pfe_cash // pfe_list[i][3]
        pfe_cash = pfe_cash - round(((pfe_cash // pfe_list[i][3]) * pfe_list[i][3]), 2)

    # If nothing else, hold.
    else:
        pass
# End for pfe_trading.

# Sell any remaining shares for cash.
pfe_cash = pfe_cash + round((pfe_shares * pfe_list[i][3]), 2)
pfe_shares = 0
print("Pfizer Part C Final:\t${:,.2f}".format(pfe_cash))

##### Part C for SPY
spy_cash = 100
spy_shares = 0
for i in range(0, len(spy_list)):

    # First day, must buy... if there is money.
    if i == 0 and spy_cash >= spy_list[i][3]:
        spy_shares = spy_cash // spy_list[i][3]
        spy_cash = spy_cash - round((spy_shares * spy_list[i][3]), 2)

    # Don't sell on the best days.
    elif spy_list[i] in spy_top5:
        next

    # Sell on the worst down days.
    elif spy_list[i] in spy_bottom5:
        spy_cash = spy_cash + round((spy_shares * spy_list[i][3]), 2)
        spy_shares = 0

    # If the price is up, sell, if there is something to sell.
    elif spy_list[i][4] > 0 and spy_shares > 0:
        spy_cash = spy_cash + round((spy_shares * spy_list[i][3]), 2)
        spy_shares = 0

    # If the price is down, buy, if there is enough money to buy.
    elif spy_list[i][4] < 0 and spy_cash >= spy_list[i][3]:
        spy_shares += spy_cash // spy_list[i][3]
        spy_cash = spy_cash - round(((spy_cash // spy_list[i][3]) * spy_list[i][3]), 2)

    # If nothing else, hold.
    else:
        pass
# End for spy_trading.

# Sell any remaining shares for cash.
spy_cash = spy_cash + round((spy_shares * spy_list[i][3]), 2)
spy_shares = 0
print("S&P 500 Part C Final:\t${:,.2f}".format(spy_cash))
