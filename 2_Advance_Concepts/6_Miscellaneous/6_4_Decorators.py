# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:33:46 2020

@author: abhi0
"""
"""
Here,make_pretty() is a decorator.
The function ordinary() got decorated and the returned function was given the name pretty.
So, The decorator acts as a wrapper.
"""

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")
    
ordinary()
# Output :
# I am ordinary

# let's decorate this ordinary function
pretty = make_pretty(ordinary)
pretty()

# Output :
# I got decorated
# I am ordinary


#===================================================================================
# Decorators : @
#===================================================================================


def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

#@smart_divide
def divide(a,b):
    return a/b
# divide=smart_divide(divide) #This assignment can be replaced 
# by the use of @ with decorator function name before the divide() definition

divide(2,0)