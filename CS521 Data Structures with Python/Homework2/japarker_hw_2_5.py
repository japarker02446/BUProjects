# -*- coding: utf-8 -*-
"""
japarker_hw_2_5.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: January 27, 2022

Execute the fizz-buzz challenge for a loop of 30 iterations.
"""

MAXVAL = 30

# For loop implementation
for i in range(1, MAXVAL+1):
    next_string = ''
    if(i % 2 == 0):
        next_string += "foo"
    if(i % 3 == 0):
        next_string += "bar"
    if(i % 5 == 0):
        next_string += "baz"
    print(i, ": ", next_string)

print()

# While loop implementation
i = 1
while i <= MAXVAL:
    next_string = ''
    if(i % 2 == 0):
        next_string += "foo"
    if(i % 3 == 0):
        next_string += "bar"
    if(i % 5 == 0):
        next_string += "baz"
    print(i, ": ", next_string)
    i += 1
