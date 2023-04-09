# -*- coding: utf-8 -*-
"""
japarker_hw_5_1.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 17, 2022

Prompt the user for the name of a text file, until a valid file is entered.
Pass the file name to a function, count the numbers of vowels and consonants.
Print the total count of vowels and consonants in the file.
"""
# Import needed modules.
from os.path import exists
import string

# Initialize constant variables
VOWELS = set('AEIOU')
CONSONANTS = set(string.ascii_uppercase) - VOWELS

# Define functions
def vc_counter(filename:str)-> dict:
    """
    Read the lines of the file.
    Parse the content and count the number of consonants and vowels to a
        dictionary object.
        
    Parameters
    ----------
    filename : str
        A valid file name.
    Returns
    -------
    dict
        Return the dictionary with consontant and vowel counts.
    """
    # Initalize function variables.
    letter_count_dict = dict(consonants = 0, vowels= 0)
    
    # Open the file, process lines of text to count letters.
    # If it is not a text file there will be an error in reading the lines.
    infile = open(filename, "r")
    try:
        infile.readline()
    except UnicodeDecodeError:
        print (filename, " is not a text file.")
        return False
    
    # If it is a text file.
    for line in infile:
        for char in line:
            if(char.upper() in CONSONANTS):
                letter_count_dict["consonants"] += 1
            elif char.upper() in VOWELS:
                letter_count_dict["vowels"] += 1
        # End for char in line
    # End for line in infile
    
    # End file functionality, close file and return counts.
    infile.close()
    return letter_count_dict
# End def vc_counter
    

# Set main program variables.
input_pass = False
letter_count_dict = dict()

# Prompt the user to enter the name of a valid (text) file.
# Pass the file name to the vc_counter function, results returned to a
#   dict object.
# If the file is not a text file the dict object will be returned with
#    a value of False.
# Pretty print the name of the file, number of consonants and number of vowels.
while not input_pass:
    input_pass = True
    user_input = input("Please enter the name of an existing text file: ")
    if exists(user_input):
        letter_count_dict = vc_counter(user_input)
        if(letter_count_dict):
            print("Total number of vowels in the text file: {:,}"\
                  .format(letter_count_dict["vowels"]))
            print("Total number of consonants in the text file: {:,}"\
                  .format(letter_count_dict["consonants"]))
        else:
            input_pass = False
    else:
        input_pass = False
        print("Sorry, I could not find that file.")
