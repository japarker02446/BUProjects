# -*- coding: utf-8 -*-
"""
japarker_hw_2_3.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: January 27, 2022

Prompt the user for a number.  Calculate the cube of that number divided by 
the number.  Print the formula and result using the entered value, limited
to two decimal places.

# REFERENCE: https://pythonguides.com/python-print-2-decimal-places/
"""

user_num = float(input("Please enter a number: "))
format_val = "{:.2f}".format(user_num**3/user_num)
print (user_num, "**3/", user_num, " = ", format_val)
