# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:54:52 2020

@author: abhi0
"""

#===================================================================================
# Generator to Reverse a string
#===================================================================================

def rev_str(my_str):
    length = len(my_str)
    a=[]
    for i in range(length - 1,-1,-1):
        a.append(my_str[i])
        yield my_str[i]
    
    

for char in rev_str("hello"):
     print(char)
# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
     
     
# This is equivalent to the for loop above, if the next() statement is executed multiple times     
d=rev_str("hello")
next(d)

# print(d) # Print just return the Generator Object desc

#===================================================================================
# Generator to Yield ACCUMULATED list in each iteration
#===================================================================================

def rev_str(my_str):
    length = len(my_str)
    a=[]
    for i in range(length - 1,-1,-1):
        a.append(my_str[i])
        yield a
    # The below yield will execute after all the yields inside the loop
    # i.e, after the yield of each iteration is executed.
    #yield a

for char in rev_str("hello"):
     print(char)
     
# For loop to reverse the string
# Output:
# ['o']
# ['o', 'l']
# ['o', 'l', 'l']
# ['o', 'l', 'l', 'e']
# ['o', 'l', 'l', 'e', 'h']


# This is equivalent to the for loop above, if the next() statement is executed multiple times
s="hello"     
d=rev_str(s)
# next(d) # Execute this Print() 5 times or else create a loop to execute it 5 times 
for i in range(len(s)):
    print(next(d))


#===================================================================================
# Generator Understanding I
#===================================================================================

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
lst_sq = [x**2 for x in my_list]
print(type(lst_sq))
print(lst_sq)

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
gen_sq = (x**2 for x in my_list)

print(type(gen_sq))
# Output: <class 'generator'>

print(gen_sq)
# Output: <generator object <genexpr> at 0x000001C6FFB12048>

print(next(gen_sq))
# Output: 1

print(next(gen_sq))
# Output: 9

print(next(gen_sq))
# Output: 36

print(next(gen_sq))
# Output: 100

print(next(gen_sq))
# Output: StopIteration

#===================================================================================
# Generator Understanding I
#===================================================================================

my_list = [1, 3, 6, 10]

# Generator Expression
sum(x**2 for x in my_list)
#146

max(x**2 for x in my_list)
#100


my_list = [1, 3, 6, 11]

# List Comprehension
sum([x**2 for x in my_list])
#167

max([x**2 for x in my_list])
#121
