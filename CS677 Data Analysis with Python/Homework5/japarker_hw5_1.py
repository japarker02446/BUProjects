# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 15, 2022
Homework Problem 5.1

Read the Fetal Cardiotocography data set from the raw Excel data file.
Remove incomplete data rows.
Combine NSP labels into two groups: N(ormal) = 1 and all others as Abnormal = 0.

Save this modified data frame back to a file for later use.
"""
import numpy as np
import os
import pandas as pd

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW5')

# Load the Excel data file into a Pandas dataframe.
# Remove rows with no FileName value (not real data rows).
xldf = pd.read_excel("CTG.xls", sheet_name="Raw Data")
xldf = xldf[xldf.FileName.notna()]

# Create a new Class column to differentiate the NSP values into:
#   N(ormal) = 1
#   S or P (Abnormal) = 0
xldf["class_label"] =  np.where(xldf.NSP == 1, 1, 0)

# Save the data frame for later use.
xldf.to_csv('GTG_clean.csv', index = False)
