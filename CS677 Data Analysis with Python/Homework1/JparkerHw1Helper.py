# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: March 17, 2022
Homework Problem 1.*

Support function to read and parse stock data from a pre-downloaded file.

WARNING: IF you are running this in an IDE you need to change the path of the
working directory manually below.  The __file__ variable is set when running
python as a script from the command line.
REFERENCE: https://stackoverflow.com/questions/16771894/python-nameerror-global-name-file-is-not-defined
"""
from math import sqrt
import operator
import os

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW1')

class JparkerHw1Helper (object):
    '''
        Helper class for Homework 1
    '''

    # Local function to map the day of the week to a numeric value.
    def day_map (day: str) -> int:
        '''
            Convert the day of week value to a numeric value.
            REFERENCE: https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
        '''
        return {
            'Monday': 1,
            'Tuesday': 2,
            'Wednesday': 3,
            'Thursday': 4,
            'Friday': 5
            }[day]
    # End def day_map

    # Local function to map a numeric value to day of the week.
    def day_unmap (day: str) -> int:
        '''
            Convert the day of week value to a numeric value.
            REFERENCE: https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
        '''
        return {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday'
            }[day]
    # End def day_map

    # Load the data file for a ticker.
    def load_ticker (ticker: str) -> list:
        '''
            Load the stock data for an input ticker from the previously downloaded
            file.  Parse to date, year, weekday, adjusted closing price and percent
            change.
        '''

        input_file = ticker + '.csv'
        try:
            with open(input_file) as file:
                lines = file.read().splitlines()
            print('Opened file for ticker: ', ticker)

        except Exception as e:
            print(e)
            print('Failed to read stock data for ticker: ', ticker)

        # Parse the lines list by Year and Weekday.  Push useful values to a new list.
        # Skip the header row.
        #
        # [0] Date  - THIS IS OUR SORT VALUE
        # [1] Year  - THIS IS A KEY
        # [2] Month
        # [3] Day
        # [4] Weekday  - THIS IS A KEY
        # [5] Week_Number
        # [6] Year_Week
        # [7] Open
        # [8] High
        # [9] Low
        # [10] Close
        # [11] Volume
        # [12 Adj Close - THIS IS OUR VALUE
        # [13] Return
        # [14] Short_MA
        # [15] Long_MA
        full_list = list()
        for i in range(1, len(lines)):
            full_list.append([lines[i].split(',')[0].replace('-',''), # Date as YYYYMMDD
                              int(lines[i].split(',')[1]),            # Year as int
                              JparkerHw1Helper.day_map(lines[i].split(',')[4]),        # Numeric day of week
                              float(lines[i].split(',')[12])])        # Adj close as float

        # Calculate the daily return values.  Store positive and negative changes
        # in new lists.
        #
        # Daily return = ((close.today - close.previous) / close.previous) * 100
        #
        # Sort the parsed list by date.  This will order the values regardless of
        # weekends or holidays.
        full_list = sorted(full_list, key=operator.itemgetter(1))
        for i in range(0, len(full_list)):
            if i == 0:
                full_list[0].append(0)
            else:
                full_list[i].append(                                \
                    (                                               \
                        (full_list[i][3] - full_list[i - 1][3]) /   \
                                   full_list[i - 1][3]              \
                    ) * 100                                         \
                )
        return full_list
    # End def load_ticker

    def calc_table_row(values: list) -> tuple:
        '''
            Calculate and return the mean, standard deviation and count for a
            list of values.

        Parameters
        ----------
        values : list
            List of input values.

        Returns
        -------
        tuple
            A three value list of the mean, standard deviation and count
            of values in the input list.
        '''
        running_sum = 0
        running_squares = 0
        count = len(values)

        # Sum values, squares of values and dt
        for i in range(0, len(values)):
            running_sum += values[i]
            running_squares += values[i]**2

        # Calculate the mean and standard deviation.
        mean = running_sum / count
        variance = (running_squares / count) - mean**2
        sd = sqrt(variance)

        return (mean, sd, count)
    # End def calc_table_rows

    def print_values_table (filename: str, table:list) -> None:
        '''
            Print a table of calculated stock values to a .csv file.

        Parameters
        ----------
        filename : str
            Name of the output file.
        table : list
            Table of values to print.  These are the stock values for HW 1 in
            the order of mean, standard deviation and count for all, negative and
            positive values.

        Returns
        -------
        None
            DESCRIPTION.

        '''
        with open(filename, 'w') as f:
            f.write("Day, mean(R), sd(R), |R|,"+ \
                    "mean(R-), sd(R-), |R-|, mean(R+), sd(R+), |R+|\n")
            for item in table:
                item = str(item).replace("[","").\
                                replace("]","").\
                                replace("(","").\
                                replace(")","")
                f.write("%s\n" % item)
        print ("Values written to " + filename)
    # End print_values_table