# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:54:34 2020

@author: abhi0
"""

#===================================================================================
# Binary Search
#===================================================================================
def binary_search(data, elem):

    low = 0
    high = len(data) - 1

    while low <= high:
      
        middle = (low + high)//2
       
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return -1
    
#===================================================================================
# create a new list called "newlist" out of the list "numbers",
# which contains only the positive numbers from the list, as integers.
#===================================================================================
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
print(newlist)

# Traditional Way Loopping
for i in numbers:
    if i > 0:
        newlist.append(i)
print(newlist)

# list comprehension
# This one is not working
# c=[newlist.append(i) for i in numbers if i > 0]
# print(c)
# This is working
newlist = [int(x) for x in numbers if x > 0]
print(newlist)

#===================================================================================
'''
The goal is to create a dictionary that maps each item in the input list 
to the item’s index in that very list. This dictionary can then be used 
to look up indices using items as keys
input = ['Duration', 'F0', 'F1', 'F2', 'F3']
output = {'Duration': 0, 'F0': 1, 'F1': 2, 'F2': 3, 'F3': 4}
'''
#===================================================================================
input = ['Duration', 'F0', 'F1', 'F2', 'F3']
dct={}
# Through traditional Looping
for i,itm in enumerate(input):
    # print(i)
    # print(itm)
    dct[itm] = i
    print('inside the loop ',i, dct)
print('Final dictionary',dct)

# Dictionary Comprehension works
print({itm:i for i,itm in enumerate(input)})
# List Comprehension works
print([itm for i,itm in enumerate(input)])

# Comprehension does not work with Tuples
print((itm for i,itm in enumerate(input)))


# Magical Behaviour of Enumerate
print(dict(enumerate(input)))
print(list(enumerate(input)))
print(tuple(enumerate(input)))

# Enumerate does not work for string
print(str(enumerate(input)))


#===================================================================================
# List Comprehension to print all the OSErrors
#===================================================================================

import os
import errno

# A Dictionary is created with errocode as key and error name as value
print({i: os.strerror(i) for i in sorted(errno.errorcode)})

#===================================================================================
# Return a new dictionary
#===================================================================================

marks = {}.fromkeys(['Math','English','Science'], 0)
print(marks)

#===================================================================================
# Unpacking Nested Data Structures in Python
#===================================================================================

a, b, c = 1, 2, 3
print(type(a))
print(type(b))
print(type(c))
a, *b, c = 1, 2, 3,4
print(type(a))
print(type(b))
print(type(c))


animals = [
   'bird',
   'fish',
   'elephant']

for f, *_, l in animals:
    print(f, l)
    
for i,itm in enumerate(animals):
    print(i, itm)
    
# This produces error    
for i,itm in animals:
    print(i, itm)
    
#===================================================================================
# Taking input for a specified no. of times, provided in range()
#===================================================================================

sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(4)]
sides

#===================================================================================
# Looping Over Two Lists : "ZIP"
#===================================================================================

# Create a list of length 3:
colour = ['Red', 'Black', 'White']

# Create a list of length 4:
units = [2,1,6]

# For each element in the first list,
for color, unit in zip(colour, units):
    # Display the corresponding index element of the second list:
    print(' The no. of {} balls is {}. '.format(color,unit))
    
# For each element in the first list,
for common in zip(colour, units):
    # Display the corresponding index element of the second list:
    print(' Both ', common)

# Return a list of pairs    
list(zip(colour, units))

# Return a tuple of pairs  
tuple(zip(colour, units))   

a=[] 
# For each element in the first as well 2nd list
for i, (color, unit) in enumerate(zip(colour, units)):
    # Display the corresponding index element of the second list:
    print('Colour no {} is {}. The no. of {} balls is {}. '.format(i,color,color,unit))
    a.append((color,unit))
print(a)

#===================================================================================
# Replacement of Enumerate and Zip : This is an Alternate of Above step
#===================================================================================

data1 = [3,4,5,7]
data2 = [4,6,8,9]
for index, value1 in enumerate(data1):
    print(index, value1 + data2[index])
  
    
#===================================================================================
# Untested : Not working
#===================================================================================

'''
If you're working with last lists and/or memory is a concern,
using the itertools module is an even better option.
'''
from itertools import izip, count
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, a, b in izip(count(), alist, blist):
    print(i, a, b)
    
#===================================================================================
# Sorting
# sort()   : list.sort(key=..., reverse=...) 
# sorted() : sorted(list, key=..., reverse=...)
#===================================================================================
    
# Input : [('g',2),('a',9),('m',3),('d',5)]
# Expected Output : [('a', 9), ('d', 5), ('g', 2), ('m', 3)]    
lst=[('g',2),('a',9),('m',3),('d',5)]
lst.sort()
lst

# Expected Output : [('m', 3), ('g', 2), ('d', 5), ('a', 9)]
lst.sort(reverse=True)
lst
print(sorted(lst, reverse=False))
print(sorted(lst, reverse=True))

#===================================================================================
# Sorting on the 2nd element ::: key function
#===================================================================================

# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
random.sort(key=takeSecond)
# print list
print('Sorted list:', random)

#===================================================================================
# Sorting in Increasing/Decreasing order of Length ::: key function
#===================================================================================

# Sorting in Increasing order of Length
country = ['Spain', 'Germany', 'Nepal', 'Australia']
country.sort(key=len)
print('Sorted list:', country)

# Sorting in Reverse order of Length
country = ['Spain', 'Germany', 'Nepal', 'Australia']
country.sort(key=len, reverse=True)
print('Sorted list:', country)

  
#===================================================================================
# Chain Together Lists
#===================================================================================

from itertools import chain
# Create a list of allies
allies = ['Spain', 'Germany', 'Namibia', 'Austria']

# Create a list of enemies
enemies = ['Mexico', 'United Kingdom', 'France']
#Iterate Over Both Lists As A Single Sequence
# For each country in allies and enemies
for country in chain(allies, enemies):
    # print the country
    print(country)
    
#===================================================================================
# Finding the index of the min/max item in an iterable ::: index()
#===================================================================================

a = [2, 3, 1]
print(a.index(max(a)))
print(a.index(1))
print(a.index(9))

#===================================================================================
# Find the Runner-Up Score!
#===================================================================================

lst=[10,2,3,10,6,5,8,11]

z = max(lst)
while max(lst) == z:
    lst.remove(max(lst))

print(max(lst))

'''
Incomplete
'''
mx=max(lst)
for i,elm in enumerate(lst):
    if elm < mx:
        j=1
        max2=elm
        
    
    if elm != max:
        max2=elm
        #print(max2)
        a=elm
       
    if elm < mx and elm >=max2:
        runup = elm
        #print(max2)


print(max2)


#===================================================================================
# Nested Lists : Name of 2nd highest marks scorer
#===================================================================================

nml=[]
scl=[]
for _ in range(int(input())):
    name = input()
    nml.append(name)
    score = float(input())
    scl.append(str(score))
print(type(nml)) 
print(type(scl))    
print(nml) 
print(scl)
 
scl2=scl.copy()
print(scl2)

mx1=max(scl2)
print(mx1)
while max(scl2) == mx1:
    scl2.remove(max(scl2))
mx2=max(scl2)
print(mx2)

a=[]
for i,m in enumerate(scl):
    if m == mx2:
        a.append(nml[i])
        print(a)
print(a.sort())
print(a)


#===================================================================================
# Nested Lists : Name of 2nd lowest marks scorer
#===================================================================================

nml=[]
scl=[]
for _ in range(int(input())):
    name = input()
    nml.append(name)
    score = float(input())
    scl.append(str(score))
print(type(nml)) 
print(type(scl))    
print(nml) 
print(scl)
 
scl2=scl.copy()
print(scl2)

mx1=min(scl2)
print(mx1)
while min(scl2) == mx1:
    scl2.remove(min(scl2))
mx2=min(scl2)
print(mx2)
'''
a=[]
for i,m in enumerate(scl):
    if m == mx2:
        a.append(nml[i])
        print(a)
a.sort()
'''
c= [n for i,(m,n) in enumerate(zip(scl,nml)) if m==mx2]
print('\n'.join(sorted(c)))

#===================================================================================
# Padding to make the length of LIST as 'n'
#===================================================================================
'''
I have a list [12,13,14,15] . Length currently is 4. I want it's length to be 10
So I need to add 0 as padding to it. The output should be [12,13,14,15,0,0,0,0,0,0]
'''
a=[1,2,3]
while len(a) <= 10:
    a.append(0)
print(a)

#===================================================================================
#===================================================================================

#===================================================================================

#===================================================================================
#===================================================================================

#===================================================================================

#===================================================================================

#===================================================================================

#===================================================================================

#===================================================================================

#===================================================================================

#===================================================================================
#===================================================================================

#===================================================================================
#===================================================================================

#===================================================================================
#===================================================================================

#===================================================================================
#===================================================================================

#===================================================================================

#===================================================================================

#===================================================================================
#===================================================================================
#===================================================================================

#===================================================================================

#===================================================================================
# Find all combinations of a set of lists with itertools.product
#===================================================================================

import itertools
from pprint import pprint

inputdata = [
    ['a', 'b', 'c'],
    ['d'],
    ['e', 'f'],
]
result = list(itertools.product(*inputdata))
pprint(result)

#===================================================================================
# Find the N longest lines in a file with Python
# Write a program to read a multiple line text file and write the N longest lines to a new file. 
# Where N and the file to be read are specified on the command line. 
# Optimization is important.
#===================================================================================

import sys

def main(filename=sys.argv[1], 
         N=int(sys.argv[2])):
    """Find the N longest lines in filename and write to filename + ".new"
    """
    lines = open(filename).readlines()
    lines.sort(cmp = lambda x,y: cmp(len(y), len(x)))
    open(filename+".new", "w").write("".join(lines[:N]))

if __name__ == '__main__':
    main()
    
    
# Using a heap is faster.

import sys,heapq

def main(filename=sys.argv[1],
         N=int(sys.argv[2])):
    """ Finds the N longest lines in filename and writes to filename + ".new"
    """
    heap = []
    lines = []
    lines = open(filename).readlines()
    heap = heapq.nlargest(N,lines,len)
    open(filename+".new", "w").write("".join(heap))

if __name__ == '__main__':
    main()
    
    
# Combined Test
    
    import heapq
import sys
import cProfile

filename = "saltycrane.com.access.log"
N = 20

def main():
    print "running saltycrane"
    cProfile.run('saltycrane(filename, N)')
    print "running charlie"
    cProfile.run('charlie(filename, N)')

def saltycrane(filename, N):
    """ Finds the N longest lines in filename and writes to filename + ".new"
    """
    lines = open(filename).readlines()
    lines.sort(cmp=lambda x,y: cmp(len(y), len(x)))
    open(filename+".new", "w").write("".join(lines[:N]))

def charlie(filename, N):
    """ Finds the N longest lines in filename and writes to filename + ".new"
    """
    heap = []
    lines = []
    lines = open(filename).readlines()
    heap = heapq.nlargest(N,lines,len)
    open(filename+".new", "w").write("".join(heap))

if __name__ == '__main__':
    main()
#===================================================================================

#===================================================================================

#===================================================================================
#===================================================================================

#===================================================================================
#===================================================================================

#===================================================================================
#===================================================================================

#===================================================================================
#===================================================================================

#===================================================================================