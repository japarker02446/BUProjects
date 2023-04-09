# -*- coding: utf-8 -*-
"""
japarker_hw_5_2.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 17, 2022

Program with three user defined functions to count and report letter counts
in different ways.
"""
# Import needed modules.
import string

# Initialize constant variables
LETTERS = string.ascii_uppercase

# Define functions.
def letter_counts(input_str:str) -> dict:
    """
    Take a string as input.  Count and return the frequency of each letter as
    a dictionary.

    Parameters
    ----------
    input_str : str
        A string.
    Returns
    -------
    dict
        A dictionary object with the letters of input_str as keys and the count
        of each component letter as a value.
    """
    # Initialize function variables.
    letter_count_dict = dict()
    
    for char in input_str:
        if char.upper() in LETTERS:
            if char.upper() in letter_count_dict:
                letter_count_dict[char.upper()] += 1
            else:
                letter_count_dict[char.upper()] = 1
    # End for char in input_str
    
    return letter_count_dict
# End def letter_counts

def most_common_letter(input_str:str) -> list:
    """
    Use the letter_counts function to count the instance of letters in a string.
    Return a list of the most common letter(s) in the string.
    
    Parameters
    ----------
    input_str : str
        A string.
    Returns
    -------
    list
        A list of the most common letter count followed by the most most common
        letters.
    """
    # Initialize function variables.
    max_letter_list = list()
    letter_count_dict = letter_counts(input_str)
    
    # Find the maximum letter count and the letters (keys) associated with
    # the max value.
    max_value = max(letter_count_dict.values())
    max_letter_list.append(max_value)
    for i, (key, value) in enumerate(letter_count_dict.items()):
        if value == max_value:
            max_letter_list.append(key)
    # End for key,value in enumerate.
    
    return max_letter_list
# End def most_common_letter

def string_count_histogram(input_str:str) -> str:
    """
    Use the letter_counts function to count the instance of letters in a string.
    Print the count of letters in the input string as a histogram with the
        letters in alphabetical order.
        
    Parameters
    ----------
    input_str : str
        A string.

    Returns
    -------
    str
        A string histogram of letter counts.
    """
    # Initalize function variables.
    letter_count_dict = letter_counts(input_str)
    histogram_str = ""
    
    # For each key (letter) print the letter value number of times on one line.
    for keys in sorted(letter_count_dict.keys()):
        for i in range(0,letter_count_dict[keys]):
            histogram_str += keys
        histogram_str += "\n"
    return histogram_str
# End def string_count_histogram

# Main program block
if __name__ == '__main__':
    
    # Initialize variables.
    SENTENCE = "this is a test sentence of at least fifteen characters"
    letter_str = ""
    most_common_list = []
    
    # Print the sentence being processed.
    print("The string being analyzed is: \"", SENTENCE, "\"", sep="")
    
    # Print the list of letters and counts not as a dict.
    # Reusing code from homework 4, problem 4.
    for i, (key, value) in enumerate(sorted(letter_counts(SENTENCE).items())):
        letter_str += key + ":" + str(value) + ", "
    letter_str = letter_str.strip(", ")
    print("1. Letter counts:", letter_str)
    
    # Print the letter(s) with maximum count.
    most_common_list = most_common_letter(SENTENCE)
    if len(most_common_list) == 2:
        print("2. Most frequent letter ", most_common_list[1], " appears ", \
              most_common_list[0], " times.")
    else:
        print("2. Most frequent letters \'", "\', \'".join(most_common_list[1:]),\
              "\' each appear ", most_common_list[0], " times.", sep="")

    # Print the letter histogram.
    print("3. Histogram: \n", string_count_histogram(SENTENCE), sep="")
