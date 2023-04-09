# -*- coding: utf-8 -*-
"""
japarker_hw_5_3.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 17, 2022

Ask the user to enter four delimited numbers, prompt for the delimiter.
Check for valid input.
Calculate the following:
    ((FIRST * SECOND) + THIRD) / FOURTH
Evaluate and catch the following errors.  If any occur, prompt the user
for a new set of numbers:
    ValueError
    ZeroDivisionError
    IndexError
"""
# Prompt the user to enter an acceptable list of four numbers.
input_pass = False
while not input_pass:
    input_pass = True
    num_list = list()
    user_input = input("Enter four numbers separated by COMMAS (negative and" \
                       "floating point is OK!): ")

    # Perform all validation checks in one block.
    # Print useful error messages as needed.
    user_input = user_input.split(",")
    try:
        for input_value in user_input:
            num_list.append(float(input_value))
        value = ((num_list[0] * num_list[1]) + num_list[2])/num_list[3]
        print("Your value is:(({:,.1f} * {:,.1f}) + {:,.1f}) / {:,.1f} = {:,.1f}".\
              format(num_list[0], num_list[1], num_list[2], num_list[3],value))
    except IndexError:
        print("You did not enter four numbers.")
        input_pass = False
    except ValueError:
        print ("One of your values is not a number:", input_value)
        input_pass = False
    except ZeroDivisionError:
        print ("Sorry, your last value cannot be zero.")
        input_pass = False
