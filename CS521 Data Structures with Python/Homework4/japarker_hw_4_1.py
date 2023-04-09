# -*- coding: utf-8 -*-
"""
japarker_hw_4_1.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 10, 2022

Use the range function to generate a list of the integers from 55 to 5 by 10s.
Calculate a new list, summing neighboring values of the first list.
Print both lists with descriptors.
"""

START_INT = 55
END_INT = 5

IN_LIST = [i for i in range(START_INT, END_INT-1, -10)]
NEW_LIST = []

# Iterate et calculate.
for i in range(0, len(IN_LIST)):
    
    # Don't run off the ends
    if i == 0 and len(IN_LIST) > 1:
#        print("1:", i)
        NEW_LIST.append(IN_LIST[i] + IN_LIST[i + 1])
    elif i == len(IN_LIST)-1:
#        print("2:", i)
        NEW_LIST.append(IN_LIST[i-1] + IN_LIST[i])
    else:
#        print("3:", i)
        NEW_LIST.append(IN_LIST[i-1] + IN_LIST[i] + IN_LIST[i + 1])

# Print the lists.
print("Input list: ", IN_LIST)
print("Result list: ", NEW_LIST)
