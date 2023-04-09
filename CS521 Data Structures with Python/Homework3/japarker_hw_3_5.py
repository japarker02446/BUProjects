# -*- coding: utf-8 -*-
"""
japarker_hw_3_5.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 3, 2022

Read the contents of a student record file.
    Read each row into a tuple.
    Store each tuple into a single list.
    Print the LIST of tuple values.
"""
# Import needed modules.
from os.path import exists

# Initialize variables
INPUT_FILE = "cs521_3_5_input.txt"
student_tuple = ()
student_list = []

# Open and read the content of the input file.
if exists(INPUT_FILE):
    infile = open(INPUT_FILE, "r")
    for line in infile:
        student_tuple = line.strip().split(',')
        student_list.append(student_tuple)
    infile.close()
    print("Student records: ", student_list)
else:
    print("ERROR: input file ", INPUT_FILE, " not found.")
