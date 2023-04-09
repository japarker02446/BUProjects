# -*- coding: utf-8 -*-
"""
japarker_hw_2_4.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: January 27, 2022

Prompt the user for a number.
Convert the number to an integer.
Print 0 if the input is even, or 1 if the input is odd.
"""

user_num = input("Please enter a number: ")
user_num = int(user_num)
print("Your number is even (0) or odd (1): ", user_num % 2)
