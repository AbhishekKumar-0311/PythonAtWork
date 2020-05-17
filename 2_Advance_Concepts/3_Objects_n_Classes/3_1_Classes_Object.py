# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:44:29 2020

@author: abhi0
"""
"""
# An object is an instance of a class.
# An object consist of data and functions(called methods) that work with data
# In Python everything is an Object
# The data of the string object is the actual characters that make up the string
# The methods are like lower replace and split.
# Wrapping up of data anf functions into a single unit is called Encapsulation
# There is no concept of Public,Private n Protected variables. All are Public.
"""

class add:
    ''' This class is to return the addition of arguments'''
    # __init__ is a constructor
    def __init__(self,a,b):
        self.op1=a
        self.op2=b
        
    def sum(self):
        add=self.op1 + self.op2
        print("Inside the Class:", add)
        return add

# An object is instantiated with values    
MyObj=add(10,20)
# The sum() is invoked
# The statements inside are executed and the returned result is assigned to Result
Result=MyObj.sum()
print("The Returned result from class is :", Result)


