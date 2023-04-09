# -*- coding: utf-8 -*-
"""
Sentence.py
Jefferson Parker
Class: CS 521 - Spring 1
Date: February 24, 2022

Sentence Class that evaluates and manipulates an English language sentence.
"""
# Import necessary modules.
import random
import re

class Sentence (object):
    """
    Sentence class evaluates and manipulates English language sentences.
    """
    def __init__(self, sentence:str) -> None:
        """
        Initialize the Sentence object with a sentence.
            Remove non-alphanumeric characters.
            Store the sentence string to a list object.
        """
        sentence = re.sub(r'[^\w\s]', '', sentence)
        self.sentence = sentence
        self.sentence = sentence.split()
        
    def get_all_words(self) -> list:
        """
        The words of the Sentence object as a list.
        
        Returns
        -------
        list
            The words of the Sentence object as a list.
        """
        return(self.sentence)
    
    def get_word(self, index: int) -> str:
        """
        Return the word at index from the Sentence object.

        Parameters
        ----------
        index : int
            Index of the target word.

        Returns
        -------
        str
            The word in the sentence at index.
        """
        try:
            return(self.sentence[index])
        except IndexError:
            return("")
    
    def set_word(self, index: int, new_word: str) -> None:
        """
        Set the value of the word at index to new_word.

        Parameters
        ----------
        index : int
            Index of the target word.
        new_word : str
            The new word to insert into the Sentence object.

        Returns
        -------
        None
        """
        try:
            self.sentence[index] = new_word
        except IndexError:
            pass
        
    def scramble(self) -> list:
        """
        Return the contents of the Sentence list in a random order.

        Returns
        -------
        list
            The scrambled list of Sentence words.
        """
        return(random.sample(self.sentence, len(self.sentence)))
    
    def __repr__(self) -> str:
        """
        Return a printable representation of the Sentence list object using
        the built in function.
        
        Returns
        -------
        str
            A printable representation of the object.
        """
        return(" ".join(self.sentence) + ".")
    
if __name__ == "__main__":
    starting_sentence = "This is a test sentence, for unit testing."
    new_sentence = Sentence(starting_sentence)
    
    # Use an assert to validate the set_word function.
    new_sentence.set_word(4, "foo")
    try:
        assert new_sentence.get_word(4) == "foo"
        print("Sentence.set_word set the word!")
    except AssertionError:
        print("Sentence.set_word did not set the word!")
    
    print("The original sentence was: ", starting_sentence)
    print("The scrambled sentence list is: ", new_sentence.scramble())
    print(repr(new_sentence))
