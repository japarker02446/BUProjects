# -*- coding: utf-8 -*-
"""
japarker_hw_3_1.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 3, 2022

Loop through the integers 2 - 130, inclusive
Count and report how many are:
    Even
    Odd
    Squares
    Cubes
For evens and odds, report the range.
For squares and cubes, report the list of values.
"""

# Initialize a few variables to hold values of interest.
first_even_int = 0
last_even_int = 0
count_even_int = 0
first_odd_int = 0
last_odd_int = 0
count_odd_int = 0
squares_list = []
cubes_list = []

# Use constants to hold the start and end values.
START_INT = 2
END_INT = 130

# Range from 2 to 130, inclusive
for i in range(START_INT,END_INT+1):
    #print(i)    #Make sure the loop is working, comment this out later.
    
    '''
    If i is even:
        Increment the count of evens
        Capture the first even value
        Capture the last even value
    ''' 
    if(i % 2 == 0):
        count_even_int += 1
        if(first_even_int == 0):
            first_even_int = i
        if(i > last_even_int):
            last_even_int = i
    
    '''
    If i is odd:
        Increment the count of odds
        Capture the first odd value
        Capture the last odd value
    ''' 
    if(i % 2 == 1):
        count_odd_int += 1
        if(first_odd_int == 0):
            first_odd_int = i
        if(i > last_odd_int):
            last_odd_int = i
        
    # Capture the squares and the cubes.
    if(i**2 <= END_INT):
        squares_list.append(i**2)
    if(i**3 <= END_INT):
        cubes_list.append(i**3)
#end for loop

# Print the report.
print("Checking numbers from ", START_INT, " to ", END_INT)
print("Odd (", count_odd_int, "): ", first_odd_int, "...", last_odd_int, sep="")
print("Even (", count_even_int, "): ", first_even_int, "...", last_even_int, sep="")
print("Square (", len(squares_list), "): ", squares_list, sep="")
print("Cube (", len(cubes_list), "): ", cubes_list, sep="")
