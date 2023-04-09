# -*- coding: utf-8 -*-
"""
japarker_hw_5_4.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 17, 2022

Prompt the user for a text file that contains words.
    There can be many lines and many words per line.
Remove all punctation, leaving only spaces between words.
Read the words from the file into a list.
Pass the list of words to a function that will return a list of words that
    appear in the file TWICE.
Print the list of words that appears twice.
"""
# Import needed modules.
import string
import re

# Define functions
def list_to_twice_words(input_list:list) -> list:
    """
    Find words that appear exactly twice in a list.

    Parameters
    ----------
    input_list : list
        An input word list.

    Returns
    -------
    list
        The list of words that appears twice in the input.
    """
    # Initialize function variables.
    word_count_dict = dict()
    twice_words_list = list()
    
    for word in input_list:
        if word.upper() in word_count_dict:
            word_count_dict[word.upper()] += 1
        else:
            word_count_dict[word.upper()] = 1
    # End for word in input_list
    
    # Which words appear twice?
    for i, (key, value) in enumerate(word_count_dict.items()):
#        print(i, key, value)
        if value == 2:
            twice_words_list.append("".join(key))
    return twice_words_list
# End def list_to_twice_words

# Initialize program variables
word_list = list()
twice_word_list = list()
input_pass = False
while not input_pass:
    input_pass = True
    user_input = input("Please enter the name of an existing text file: ")

    # Open the file.  Catch exceptions for existence and binary content.
    # Parse the contents to a list.
    try:
        infile = open(user_input, "r")
        for next_line in infile:
            next_line = next_line.strip()

# Removing the punctuation isn't working yet
#            next_line = re.sub([string.punctuation], " ", next_line)

            word_list.extend(next_line.split())

        infile.close()
        twice_word_list = list_to_twice_words(word_list)
        print("The list of words that appears twice is: ", twice_word_list)
            
    except FileNotFoundError:
        print("File does not exist: ", user_input)
        input_pass = False
        
    except UnicodeDecodeError:
        print (user_input, " is not a text file.")
        input_pass = False
