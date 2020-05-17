# Python OOPS

    Python Objects and Class

        What are classes and objects in Python?

            Python is an object oriented programming language.

            Object is simply a collection of data (variables) and methods (functions) that act on those data.
            Class is a blueprint for the object.

            We can create many objects from a class. An object is also called an INSTANCE of a class.
            The process of creating this object is called INSTANTIATION.

        Defining a Class in Python

            Class definitions begin with the keyword def, Like function.

            The first string is called DOCSTRING and has a brief description about the class.
            Although not mandatory, this is recommended.

                Here is a simple class definition.

                class MyNewClass:
                    '''This is a docstring. I have created a new class'''
                    pass

            A class creates a new local namespace where all its attributes are defined.
            Attributes may be data or functions.

            There are also special attributes in it that begins with double underscores (__).
            For example, __doc__ gives us the docstring of that class.

                >>> ob = MyClass()

                This will create a new instance object named ob.
                We can access attributes of objects using the object name prefix.

            Attributes may be data or method. Method of an object are corresponding functions of that class.
            Any function object that is a class attribute defines a method for objects of that class.

            Whenever an object calls its method, the object itself is passed as the first argument.
            So, ob.func() translates into MyClass.func(ob).

            The first argument of the function in class must be the object itself.
            This is conventionally called self. Recommended to follow the convention.

        Constructors in Python

            Class functions that begins with double underscore (__) are called special functions
            as they have special meaning.

            Example __init__() function. This special function gets called
            whenever a new object of that class is instantiated.

            This type of function is also called constructors in Object Oriented Programming (OOP).
            And use it to initialize all the variables.

        Deleting Attributes and Objects

            Any attribute of an object can be deleted anytime, using the del statement.

                >>> c1 = ComplexNumber(2,3)
                >>> del c1.imag
                >>> c1.getData()
                Traceback (most recent call last):
                ...
                AttributeError: 'ComplexNumber' object has no attribute 'imag'

                >>> del ComplexNumber.getData
                >>> c1.getData()
                Traceback (most recent call last):
                ...
                AttributeError: 'ComplexNumber' object has no attribute 'getData'
                We can even delete the object itself, using the del statement.

                >>> c1 = ComplexNumber(1,3)
                >>> del c1
                >>> c1
                Traceback (most recent call last):
                ...
                NameError: name 'c1' is not defined

                When we do c1 = ComplexNumber(1,3), a new instance object is created in memory
                and the name c1 binds with it.

                On the command del c1, this binding is removed and the name c1 is deleted from the corresponding namespace.
                The object however continues to exist in memory and if no other name is bound to it, it is later automatically destroyed.

                This automatic destruction of unreferenced objects in Python is also called garbage collection.