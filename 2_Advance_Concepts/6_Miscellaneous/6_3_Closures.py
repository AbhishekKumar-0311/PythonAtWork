# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:06:55 2020

@author: abhi0
"""
"""
The criteria that must be met to create closure in Python are:

    1.We must have a nested function (function inside a function).
    2.The nested function must refer to a value defined in the enclosing function.
    3.The enclosing function must return the nested function.
    
In below code, times3 and times5 are closure functions.
"""


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)
print(type(times3))
print(times3)

nesFuc=times3(9)
print(type(nesFuc))
print(nesFuc)
# Output: 27

# Multiplier of 5
times5 = make_multiplier_of(5)

# Delete the function make_multiplier_of
del make_multiplier_of
try:
    # Calling the make_multiplier_of throws Error
    make_multiplier_of(3)
except OSError:
    print("The make_multiplier_of is deleted" )

# But still, Calling the CLOSURE FUNCTION -> times3(), 
# which Holds the Returned Sub-Fumction name EXECUTES
nesFuc=times3(11)
print(type(nesFuc))
print(nesFuc)
# Output: 33

print(times5(3))
# Output: 15

print(times5(times3(2)))
# Output: 30