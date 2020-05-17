# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:33:32 2020

@author: abhi0
"""
"""
Create a diamond shape with stars
"""

Star = int(input('Enter the no. of max stars for making diamond : '))
# print(type(Star))

k = Star

for i in range(1,Star+1,2):
    j = int((k-1)/2)
    print(' '*j,'*'*i)
    k = k-2
    
k = Star

for i in range(Star-2,0,-2):
    j = int((k-i)/2)
    print(' '*j,'*'*i)