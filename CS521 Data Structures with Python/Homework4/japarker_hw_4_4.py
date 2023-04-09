# -*- coding: utf-8 -*-
"""
japarker_hw_4_4.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 10, 2022

Using the provided dictionary, print:
    All the keys as a list
    All the values as comma separated values
    Key value pairs as formatted data (not a list)
    Key value pairs as tuples sorted by keys
    Key value pairs as formatted data (not a list)
"""

# Import module components.
from operator import itemgetter

# Initialize the variables.
MY_DICT = {'a':15, 'c':18, 'b':20}

# Print all the things
print("Keys:", list(MY_DICT.keys()))
print("Values:", ', '.join(map(str,list(MY_DICT.values()))))

# Print key value pairs as formatted text.
# this is ugly, I know.
key_value_string = ''
for i, (key, value) in enumerate( MY_DICT.items()):
    key_value_string += key + ":" + str(value) + ", "
key_value_string = key_value_string.strip(", ")
print("Key value pairs:", key_value_string)

# Tuples sorted by keys.
key_tuple = []
for i in sorted(MY_DICT.keys()):
#   print(i, ":", MY_DICT[i])
    key_tuple.append((i, MY_DICT[i]))
print("Key value pairs ordered by key:", key_tuple)

# Key value pairs sorted by values, printed as formatted text.
key_value_string = ''
value_list = list(MY_DICT.items())
value_list = sorted(value_list, key = itemgetter(1))
for i, (key, value) in enumerate(value_list):
#   print(key, value)
    key_value_string += key + ":" + str(value) + ", "
key_value_string = key_value_string.strip(", ")
print("Key value pairs ordered by value:", key_value_string)