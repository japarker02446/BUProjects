# -*- coding: utf-8 -*-
"""
japarker_hw_2_1.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: January 27, 2022

This is a program to prompt the user for a numeric input, perform a calculation
and print the results.
"""

user_num = int(input("Please enter a whole number between 1 and 7: "))
calculated_num = user_num * 2 + 10 / 2 - user_num
print("Your calculated value is: ", int(calculated_num))

# =============================================================================
# For the user supplied number, convert it to a three digit number with the 
# next two incrementing digits.  Perform additional calculations on these
# digits.
# =============================================================================

user_plus1 = user_num + 1
user_plus2 = user_num + 2
three_digit = int(str(user_num) + str(user_plus1) + str(user_plus2))

three_sum = user_num + user_plus1 + user_plus2
print("The sum of your number, plus the next two numbers, is: ", three_sum)

three_div = three_digit / three_sum
print("Your final value is: ", three_div)
print("Your final value, as an integer, is: ", int(three_div))
