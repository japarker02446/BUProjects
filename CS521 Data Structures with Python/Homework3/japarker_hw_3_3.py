# -*- coding: utf-8 -*-
"""
japarker_hw_3_3.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 3, 2022

Prompt the user to enter a three digit number , such that the digits are
in ascending order and without duplicates.  If there is an error in the
input, report an error message and repeat.
"""

# Use a while loop to repetitively prompt for input until the value is accepted
passed = False
while(passed != True):
    
    # Assume the entered value is valid.
    passed = True
    
    # Get user input value.
    input_string = input("Please enter a 3-digit integer: ")
    
    # Check the length of the input string.
    if len(input_string) != 3:
        passed = False
        print("--> Error: You did not enter a 3-digit number.")
        
    # Per character for loop
    for char in input_string:
        
        # Check for any non-digit characters (not integer).
        if not(char.isdigit()):
            passed = False
            print("--> Error: This is not an integer.")
            
        # Check for duplicate characters.
        if input_string.count(char) != 1:
            passed = False
            print("--> Error: Your number contains a duplication.")
    # end per character for loop.
    
    # Check for ascending order.
    for i in range(len(input_string)-1):
        if(input_string[i+1] < input_string[i]):
            passed = False
            print("--> Error: The digits are not in ascending order.")
# end while loop.

print("Number Accepted! ", input_string)