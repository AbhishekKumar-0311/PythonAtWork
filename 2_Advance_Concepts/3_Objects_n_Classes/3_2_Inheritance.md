# Python Inheritance

    Python Inheritance

        Inheritance enable us to define a class that takes all the functionality
        from parent class and allows us to add more.
        This results into RE-USABILITY of code.

        What is Inheritance?

            It refers to defining a new class with little or no modification to an existing class.
            The new class is called derived (or child) class
            The one from which it inherits is called the base (or parent) class.

        Python Inheritance Syntax

            class BaseClass:
                Body of base class
            class DerivedClass(BaseClass):
                Body of derived class


        Example of Inheritance in Python

            Here is an example.

            A polygon is a closed figure with 3 or more sides.

                class Polygon:
                    def __init__(self, no_of_sides):
                        self.n = no_of_sides
                        self.sides = [0 for i in range(no_of_sides)]

                    def inputSides(self):
                        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

                    def dispSides(self):
                        for i in range(self.n):
                        print("Side",i+1,"is",self.sides[i])

            This class has data attributes to store the number of sides,
            n and magnitude of each side as a list, sides.

            Method inputSides() takes in magnitude of each side and similarly,
            dispSides() will display these properly.

            A triangle is a polygon with 3 sides.
            So, we can create a class called Triangle which inherits from Polygon.
            This makes all the attributes available in class Polygon readily available in Triangle.
            We don't need to define them again (code re-usability).
            Triangle is defined as follows.

                class Triangle(Polygon):
                    def __init__(self):
                        Polygon.__init__(self,3)

                    def findArea(self):
                        a, b, c = self.sides
                        # calculate the semi-perimeter
                        s = (a + b + c) / 2
                        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
                        print('The area of the triangle is %0.2f' %area)

            However, class Triangle has a new method findArea() to find and print the area of the triangle.

                >>> t = Triangle()

                >>> t.inputSides()
                Enter side 1 : 3
                Enter side 2 : 5
                Enter side 3 : 4

                >>> t.dispSides()
                Side 1 is 3.0
                Side 2 is 5.0
                Side 3 is 4.0

                >>> t.findArea()
                The area of the triangle is 6.00

            We are able to use methods like inputSides() or dispSides() for class Triangle.

            If an attribute is not found in the class, search continues to the base class.
            This repeats recursively, if the base class is itself derived from other classes.

        Method Overriding in Python

            In the above example, notice that __init__() method was defined in both classes,
            Triangle as well Polygon.
            When this happens, the method in the derived class overrides that in the base class.
            This is to say, __init__() in Triangle gets preference over the same in Polygon.

            Generally when overriding a base method, we tend to extend the definition rather than simply replace
            it.
            Like, by calling the method in base class from the one in derived class (calling Polygon.__init__()
            from __init__() in Triangle).

            Better to use the built-in function super().
            super().__init__(3) is equivalent to Polygon.__init__(self,3) and is preferred.

            Two built-in functions isinstance() and issubclass() are used to check inheritances.
            Function isinstance() returns True if the object is an instance of the class or
            other classes derived from it.
            Each and every class in Python inherits from the base class object.

                >>> isinstance(t,Triangle)
                True

                >>> isinstance(t,Polygon)
                True

                >>> isinstance(t,int)
                False

                >>> isinstance(t,object)
                True

            issubclass() is used to check for class inheritance.

                >>> issubclass(Polygon,Triangle)
                False

                >>> issubclass(Triangle,Polygon)
                True

                >>> issubclass(bool,int)
                True

        Multiple Inheritance in Python

            A class can be derived from more than one base classes in Python.
            This is called multiple inheritance.

            In multiple inheritance, the features of all the base classes are inherited into the derived class.
            The syntax for multiple inheritance is similar to single inheritance.

            Example
                class Base1:
                    pass

                class Base2:
                    pass

                class MultiDerived(Base1, Base2):
                    pass

            Here, MultiDerived is derived from classes Base1 and Base2.


        Multilevel Inheritance in Python

            We can also inherit form a derived class. This is called multilevel inheritance.
            It can be of any depth in Python.

            In multilevel inheritance, features of the base class and the derived class
            is inherited into the new derived class.

            An example

                class Base:
                    pass

                class Derived1(Base):
                    pass

                class Derived2(Derived1):
                    pass

                Here, Derived1 is derived from Base, and Derived2 is derived from Derived1.



        Method Resolution Order in Python

            Every class in Python is derived from the class object. It is the most base type in Python.

            So technically, all other class, either built-in or user-defines, are derived classes
            and all objects are instances of object class.

            In the multiple inheritance scenario, any specified attribute is searched first in the current class.
            If not found, the search continues into parent classes in depth-first,
            left-right fashion without searching same class twice.

            So, in the above example of MultiDerived class
            the search order is [MultiDerived, Base1, Base2, object].
            This order is also called LINEARIZATION OF MULTIDERIVED CLASS
            and the set of rules used to find this order is called METHOD RESOLUTION ORDER (MRO).

            MRO must prevent local precedence ordering and also provide monotonicity.
            It ensures that a class always appears before its parents and in case of multiple parents,
            the order is same as tuple of base classes.

            MRO of a class can be viewed as the __mro__ attribute or mro() method.
            __mro__ returns a tuple.
            mro() returns a list.

                >>> MultiDerived.__mro__
                (<class '__main__.MultiDerived'>,
                <class '__main__.Base1'>,
                <class '__main__.Base2'>,
                <class 'object'>)

                >>> MultiDerived.mro()
                [<class '__main__.MultiDerived'>,
                <class '__main__.Base1'>,
                <class '__main__.Base2'>,
                <class 'object'>]

