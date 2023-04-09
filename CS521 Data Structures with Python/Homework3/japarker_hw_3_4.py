# -*- coding: utf-8 -*-
"""
japarker_hw_3_4.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 3, 2022

Read a file, cs521_3_4_input.txt.
Validate that the file contains a single sentence of 20 words.
Break the sentence into four lines of five words per line, write those
    to a new file cs521_3_4_output.txt.
"""
# Import needed modules.
from os.path import exists

# Initialize variables
INPUT_FILE = "cs521_3_4_input.txt"
OUTPUT_FILE = "cs521_3_4_output.txt"
MAX_FILE_WORDS = 20
LINE_WORDS_INT = 5

# Open and read the content of the input file.
if exists(INPUT_FILE):
    infile = open(INPUT_FILE, "r")
    all_lines_string = infile.readlines()
    infile.close()
    
    # Test that there was one sentence.
    if len(all_lines_string) != 1:
        print("ERROR: The file does not contain one sentence.")
    else:
        
        # Check that the one sentence is 20 words.
        sentence_word_list = all_lines_string[0].strip().split()
        if len(sentence_word_list) != MAX_FILE_WORDS:
            print("ERROR: The sentence does not contain 20 words.")
        else:
            
            # Split the sentence into four lines of five words, 
            # Write the lines to a new file.
            outfile = open(OUTPUT_FILE, "w")
            for i in range(4):
                new_lines = []
                for j in range(LINE_WORDS_INT):
                    new_lines.append(sentence_word_list[0])
                    sentence_word_list = sentence_word_list[1:len(sentence_word_list)]
                
                # Convert the list to a string and write to the output file.
                # REFERENCE: https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python
                line_string = ' '.join(new_lines)
                line_string += "\n"
                byte_write = outfile.write(line_string)
                if byte_write:
                    file_written = True
                else:
                    file_written = False
            # end for loop.
            
            if file_written:
                print("Success! Output written to: ", OUTPUT_FILE)
            outfile.close()

else:
    print("ERROR: input file ", INPUT_FILE, " not found.")
