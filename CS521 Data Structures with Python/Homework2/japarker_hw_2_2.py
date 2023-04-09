# -*- coding: utf-8 -*-
"""
japarker_hw_2_2.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: January 27, 2022

Prompt the user for input (string or numeric) and print the value as a string,
integer and floating point value.
"""

user_input = input("Please enter a string or number: ")
print("Your value as a string is: ", user_input)
print("Your value as an integer is: ", int(float(user_input)))
print("Your value as a float is: ", float(user_input))

"""
2.2.c.
The input function returns a string value, which will be printed without issue.

An integer input will run without issue, as this can be printed as a string or
cast to a floating point value.

Interestingly, a floating point input value will also crash if you try to cast
it to an int.  Therefore I put a double cast (first to float, then to int) 
for the 'print as an integer' line.
"""