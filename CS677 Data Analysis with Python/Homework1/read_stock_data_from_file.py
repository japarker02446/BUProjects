# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:37:29 2018

@author: epinsky
this scripts reads your ticker file (e.g. MSFT.csv) and
constructs a list of lines
"""
import os
os.path.join(os.path.dirname(__file__))
here = os.path.abspath(__file__)

ticker = 'PFE'
# input_dir = r'C:\Users\epinsky\bu\python\data_science_with_Python\datasets'
input_dir = 'C:\\Users\\jparker\\Code\\Python\\CS677\\HW1'
ticker_file = os.path.join(input_dir, ticker + '.csv')

try:
    with open(ticker_file) as f:
        lines = f.read().splitlines()
    print('opened file for ticker: ', ticker)
    """    your code for assignment 1 goes here
    """

except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)
