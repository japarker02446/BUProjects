# -*- coding: utf-8 -*-
"""
japarker_hw_3_2.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 3, 2022

Create a docstring constant of three sentences.
Parse the docstring to a list with one element per sentence.
For each sentence in the list, count and report the number of:
    uppercase letters
    lowercase letters
    digits
    punctuation characters (do not include whitespace)
"""

# import useful modules.
import string

# I had forgotten how creepy this quote actually is.
SENTENCES = """Th!s 15 my r!fl3.
Th3r3 @r3 m@ny l!k3 1t, but th!s 0ne 1s m!ne.
My r!fle 1s my b3st fr!3nd.
"""

sentence_list = SENTENCES.strip().split("\n")

# Initialize the header row for the output table.
# NOTE - Each variable column is EIGHT characters wide!
# NOTE - Each space between columns is THREE characters wide!
print("#   # Upper    # Lower    # Digits   # Punct.")
print("-   -------    -------    --------   --------")

# Quantify the table, report the values.
for i in range(len(sentence_list)):
    
    # Initialize variables for each sentence.
    upper_count_int = 0
    lower_count_int = 0
    digit_count_int = 0
    punc_count_int = 0
    
    for char in sentence_list[i]:
        if char.isupper():
            upper_count_int += 1
        if char.islower():
            lower_count_int += 1
        if char.isdigit():
            digit_count_int += 1
        if char in string.punctuation:
            punc_count_int += 1
    #end for loop char in sentence

    print(i+1, "   {:^8}   {:^8}   {:^8}   {:^8}".format(upper_count_int, lower_count_int,\
                                             digit_count_int, punc_count_int),\
          sep="")
#end for loop in range
