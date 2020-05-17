# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:49:06 2020

@author: abhi0
"""

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
        
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self,n):
        self._n=n
        #Polygon.__init__(self,3)
        # Extending the Base class __init__()
        super().__init__(self._n)
    
    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

t = Triangle(3)
t.inputSides()
t.dispSides()
t.findArea()


isinstance(t,Triangle)
isinstance(t,Polygon)
isinstance(t,int)
isinstance(t,object)

# Is Polygon a subclass of Triangle  : No
issubclass(Polygon,Triangle)
# Is Triangle a subclass of Polygon : Yes
issubclass(Triangle,Polygon)
# Is Bool a subclass of Int : Yes
issubclass(bool,int)

# Output: True
print(issubclass(list,object))

# Output: True
print(isinstance(5.5,object))

# Output: True
print(isinstance("Hello",object))

# Multiple Inhertance
# The class MultiDerived inherits from both Base1 and Base2
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

# Multilevel Inheritance
#  Derived1 is derived from Base, and Derived2 is derived from Derived1.
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass

# METHOD RESOLUTION ORDER
# In the multiple inheritance scenario, any specified attribute is searched first in the current class.
# If not found, the search continues into parent classes in depth-first, left-right fashion without searching same class twice.
# __mro__ returns a tuple
MultiDerived.__mro__
# mro() returns a list
MultiDerived.mro()
Derived2.mro()
