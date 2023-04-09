# -*- coding: utf-8 -*-
"""
japarker_hw_4_5.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 10, 2022

Convert a (negative and / or floating point) number to words.
"""

# Initialize variables.
NUM_MAP = {"1":"One",
           "2": "Two",
           "3": "Three",
           "4": "Four",
           "5": "Five",
           "6": "Six",
           "7": "Seven",
           "8":" Eight",
           "9": "Nine",
           ".": "point",
           "-": "negative"}

# Prompt the user to enter an acceptable number.
input_pass = False
while not input_pass:
    input_pass = True
    user_input = input("Enter a number (negative and floating point is OK!): ")
    for char in user_input:
        if char not in ["0","1","2","3","4","5","6","7","8","9","-","."]:
#            print("FAIL:", char)
            input_pass = False

# User input accepted.
print("As Text: ", end="")
for char in user_input:
    print(NUM_MAP[char], end=" ")
print()

    