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
