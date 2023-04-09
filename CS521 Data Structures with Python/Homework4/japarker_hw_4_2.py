# -*- coding: utf-8 -*-
"""
japarker_hw_4_2.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 10, 2022

Quantify the instance of each character in a sentence using a dictionary.
Ignore case.
Print results to output.
"""

# Import modules
import string

# Intiialize variables
SENTENCE = "The rain in Spain falls mainly on the plain."
count_dict = dict()

# Case doesn't matter, make them all uppercase
# Remove any punctuation characters.
# Remove space characters.
working_sentence = SENTENCE.upper()
working_sentence = working_sentence.strip(string.punctuation)
working_sentence = working_sentence.replace(" ", "")

# Count the instances of each character in working_sentence.
for char in list(working_sentence):
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1
        
# Get the character(s) that have the maximum count.
count_max = max(list(count_dict.values()))
chars_max = list()

for char in count_dict.keys():
#    print(char, " ", count_dict[char])
    if count_dict[char] == count_max:
        chars_max.append(char)

print("The string being analyzed is: \"", SENTENCE, "\"", sep="")
print("1. Dictionary of letter counts: ", count_dict)
print("2. Most frequent letter(s)", chars_max, "appear", count_max, "times")