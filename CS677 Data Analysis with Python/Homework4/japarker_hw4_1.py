# -*- coding: utf-8 -*-
"""
Jefferson Parker
Class: CS 677
Date: April 7, 2022
Homework Problem 4.1

Load the heart failure data into a pandas data frame, split by death event,
plot correlation matrix plots to files.
"""
import matplotlib.pyplot as plt
import os
import seaborn as sns

# Set the input directory path.
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    os.chdir(r'C:\Users\jparker\Code\Python\CS677\HW4')

# Import helper functions to heart data from file.
from JparkerHw4Helper import *

# Question 1.1
# Load the heart failure data set from a text file to a pandas dataframe.
# Split into death event = 0 (living) or death event = 1 (dead).
fail_data = JparkerHw4Helper.load_data()
fail0_data = fail_data.loc[fail_data.DEATH_EVENT == 0]
fail1_data = fail_data.loc[fail_data.DEATH_EVENT == 1]

# Question 1.2
# Save correlation matrix plots to pdf files.
M0 = fail0_data.corr().round(3)
plt.figure(figsize = (10, 7.5))
corr_plot = sns.heatmap(M0, cmap="Blues", annot = True)
plt.savefig('japarker_hw4_death0.pdf')

M1 = fail1_data.corr().round(3)
plt.figure(figsize = (10, 7.5))
sns.heatmap(M1, cmap="Blues", annot = True)
plt.savefig('japarker_hw4_death1.pdf')

# Question 1.3
# Features with high correlation for survival (M0): sex x smoking - 0.49
# Features with low correlation for survival (M0): serum creatinine x time - 0
# Features with high correlation for death (M1): sex x smoking - 0.36
# Features with low correlation for death (M1): serum sodium x diabetes - -0.008
# The results are same for high correlation, but different for low correlation
