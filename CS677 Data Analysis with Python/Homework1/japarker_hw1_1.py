# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: March 17, 2022
Homework Problem 1.1

Read historical stock data (PFE.txt) and report summary data per year.
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

# Load the data for PFE (Pfizer Inc).
# load_ticker() returns a list of lists including:
#   Datestamp,
#   Year
#   Numeric day of week
#   Adjusted closing price
#   Percent day return
pfe_list = JparkerHw1Helper.load_ticker('PFE')

# Sort the list by year, day of week and date.
pfe_list = sorted(pfe_list, key=operator.itemgetter(1,2,0))

# Calculate the mean and standard deviation percent gains by year and weekday
# for all, positive and negative percent changes.
#
# The list is sorted by year and day of week.
# Capture the running sum, sum of squares and count of adjusted gains.
now_year = pfe_list[0][1]
now_day = pfe_list[0][2]

all_vals = list()
pos_vals = list()
neg_vals = list()
print_table = list()

for i in range(0, len(pfe_list)):
#   print (pfe_list[i], now_year, now_day, len(all_vals))

    if pfe_list[i][1] == now_year:
        if pfe_list[i][2] == now_day:
            all_vals.append(pfe_list[i][4])
            if pfe_list[i][4] > 0:
                pos_vals.append(pfe_list[i][4])
            if pfe_list[i][4] < 0:
                neg_vals.append(pfe_list[i][4])

        else:
            # Capture values for the year and day of week.
            print_table.append([JparkerHw1Helper.day_unmap(now_day),
                                JparkerHw1Helper.calc_table_row(all_vals),
                                JparkerHw1Helper.calc_table_row(neg_vals),
                                JparkerHw1Helper.calc_table_row(pos_vals)]
                              )

            # Reset for the next day.
            all_vals = list()
            pos_vals = list()
            neg_vals = list()

            now_day = pfe_list[i][2]
        # End if-else now_day

    else:
        # Capture values for the end of the year.
        print_table.append([JparkerHw1Helper.day_unmap(now_day),
                            JparkerHw1Helper.calc_table_row(all_vals),
                            JparkerHw1Helper.calc_table_row(neg_vals),
                            JparkerHw1Helper.calc_table_row(pos_vals)]
                          )

        file_name = 'PFE_' + str(now_year) + '.csv'
        JparkerHw1Helper.print_values_table(file_name, print_table)

        # Reset for the next year (and day).
        all_vals = list()
        pos_vals = list()
        neg_vals = list()
        print_table = list()

        now_year = pfe_list[i][1]
        now_day = pfe_list[i][2]
    # End if-else now_year

# Flush the values to the print table.
print_table.append([JparkerHw1Helper.day_unmap(now_day),
                    JparkerHw1Helper.calc_table_row(all_vals),
                    JparkerHw1Helper.calc_table_row(neg_vals),
                    JparkerHw1Helper.calc_table_row(pos_vals)]
                  )

file_name = 'PFE_' + str(now_year) + '.csv'
JparkerHw1Helper.print_values_table(file_name, print_table)
