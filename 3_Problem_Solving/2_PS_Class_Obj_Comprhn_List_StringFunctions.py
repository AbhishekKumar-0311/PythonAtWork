# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:23:39 2020

@author: abhi0
"""
"""
Create a class called Analyzer that performs some simple analysis on a string.
Create methods to return how many words are in the string, how many are of a
given length, and how many start with a given string.
"""
from string import punctuation

class Analyzer:
    def __init__(self, s):
        for c in punctuation:
            # .replace : Replaces all punctuation characters with the 2nd argument of the func
            s = s.replace(c,'')
            # print(c,s)
        
        s = s.lower()
        # print(s)
        self.words = s.split()
        # print(type(self.words))
        
    def number_of_words(self):
        return len(self.words)
    
    def starts_with(self, s):
        return len([w for w in self.words if w[:len(s)]==s])
    
    def number_with_length(self, n):
        return len([w for w in self.words if len(w)==n])
    
s = 'This is a test of the class.'
analyzer = Analyzer(s)
print(analyzer.words)
print('Number of words:', analyzer.number_of_words())
print('Number of words starting with "t":', analyzer.starts_with('t'))
print('Number of 2-letter words:', analyzer.number_with_length(2))
