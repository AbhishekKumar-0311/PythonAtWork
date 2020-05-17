# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:15:28 2020

@author: abhi0
"""

import re

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)

if match:
    print(match.group())
else:
    print("pattern not found")
print(type(match))    
print(type(match.group()))
print(match.group(1))
print(match.group(2))
print(match.start())
print(match.end())
print(match.span())


# Create a variable containing a text string
text = 'The quick brown fox jumped over the lazy brown bear.'

# Find any word of three letters
pattern1=r'\b...\b'
re.findall(pattern1, text)
match=re.search(pattern1, text)
print(match.group())

#===================================================================================
# Testing begin
#===================================================================================
pattern2='^\w{3}'
re.findall(pattern2, text)
match=re.search(pattern2, text)
print(match.group())

pattern3='......'
re.findall(pattern3, text)
match=re.search(pattern3, text)
print(match.group())

pattern3='\w{6}'
re.findall(pattern3, text)
match=re.search(pattern3, text)
print(match.group())

#===================================================================================
# Testing end
#===================================================================================


text = 'The quick brown fox jumped overui the lazy brown bear.'
pattern3='\w{6}'
# Find all the six letter word
re.findall(pattern3, text)
# Find First occurrence of the six letter word
match=re.search(pattern3, text)


pattern4=re.compile('.*\w{6}.*')
match=pattern4.match(pattern3, text)
print(match)