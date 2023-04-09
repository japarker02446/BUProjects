# -*- coding: utf-8 -*-
"""
japarker_hw_5_5.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 17, 2022

Write a program that calculates N factorial with and without recursion.
"""
def factorial(value: int) -> int:
    """
    Calculate the factorial of a value.

    Parameters
    ----------
    value : int
        The input number.

    Returns
    -------
    int
        The input number multiplied by (input value - 1).
    """
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)
# End def factorial

def factorial2(value:int) -> int:
    """
    Calculate the factorial of a value without recursion.

    Parameters
    ----------
    value : int
       The input number.

    Returns
    -------
    int
       The input number factorial.
    """
    factorial_int = 1
    for i in range(value):
        factorial_int *= (value - i)
    return factorial_int
# End factorial2

input_pass = False
while not input_pass:
    input_pass = True
    try:
        user_num = int(input("Please enter a integer value: "))
        print("Call to recursive factorial is: {:,}".format(factorial(user_num)))
        print("Call to non-recursive factorial2 is: {:,}".format(factorial2(user_num)))
    except ValueError:
        print("You did not enter an integer value.")
        input_pass = False