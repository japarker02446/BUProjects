# -*- coding: utf-8 -*-
"""
japarker_hw_4_3.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 10, 2022

Create two constant lists, one of first names and one of last names.
Validate that the last name list is at least as long as the first name list.
    If not, exit with an error message.
Use the zip function to create a dictionary with the last names as keys and 
    first names as values. Set missing first names to None (None object, not
    not a string).  
Print the lists of first names, last names and combination.
"""
# Import modules
import sys

# Intialize variables
FIRST_NAMES = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer"]
#SHORT_LAST= ["Smith", "Johnson", "Williams", "Brown", "Jones"]
#LONG_LAST = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"\
#             "Davis", "Rodriguez", "Martinez"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]

# Check the lengths.
# If there are more first names, exit (try to make it graceful).
# If there are more last names, pad the list of first names with None objects.
if len(FIRST_NAMES) > len(LAST_NAMES):
    sys.exit("Error, Last names must be at least as long as first names.")
elif len(FIRST_NAMES) < len(LAST_NAMES):
    FIRST_NAMES.extend([None] * (len(LAST_NAMES) - len(FIRST_NAMES)))

# Merge the lists into a dictionary.
names_dict = dict(zip(LAST_NAMES, FIRST_NAMES))

# Print
print("First names:", FIRST_NAMES)
print("Last names:", LAST_NAMES)
print("Name dictionary:", names_dict)
