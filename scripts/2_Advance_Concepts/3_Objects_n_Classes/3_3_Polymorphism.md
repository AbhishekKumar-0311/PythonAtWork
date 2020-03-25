# Python Polymorphism

    Polymorphism in Python

        What is Polymorphism?

            Polymorphism is the ability of an object to take on many forms.
            It refers to the use of a single type entity (method, operator or object)
            to represent different types in different scenarios.

                Example 1: Polymorphism in addition operator

                    For integer data types, + operator is used to perform arithmetic addition operation.

                    num1 = 1
                    num2 = 2
                    print(num1+num2)

                    The above program outputs 3.

                    Similarly, for string data types, + operator is used to perform concatenation.

                    str1 = "Python"
                    str2 = "Programming"
                    print(str1+" "+str2)

                    The above program outputs Python Programming.

            Function Polymorphism in Python

                There are some functions in Python which are compatible to run with multiple data types.

                    Ex: len() function which can run with many data types in Python.

                    Example 2: Polymorphic len() function
                    print(len("Programiz"))
                    print(len(["Python", "Java", "C"]))
                    print(len({"Name": "John", "Address": "Nepal"}))
                    Run Code
                    Output

                    9
                    3
                    2

                    Many data types such as string, list, tuple, set, and dictionary
                    can work with the len() function.

            Class Polymorphism in Python

                We can use the concept of polymorphism while creating class methods as
                Python allows different classes to have methods with the same name.

                We can then later generalize calling these methods by disregarding the object we are working with.

                Example 3: Polymorphism in Class Methods

                    class Cat:
                        def __init__(self, name, age):
                            self.name = name
                            self.age = age

                        def info(self):
                            print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

                        def make_sound(self):
                            print("Meow")

                    class Dog:
                        def __init__(self, name, age):
                            self.name = name
                            self.age = age

                        def info(self):
                            print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

                        def make_sound(self):
                            print("Bark")

                    cat1 = Cat("Kitty", 2.5)
                    dog1 = Dog("Fluffy", 4)

                    for animal in (cat1, dog1):
                        animal.make_sound()
                        animal.info()
                        animal.make_sound()

                    Output

                        Meow
                        I am a cat. My name is Kitty. I am 2.5 years old.
                        Meow
                        Bark
                        I am a dog. My name is Fluffy. I am 4 years old.
                        Bark

                    Here, we have created two classes Cat and Dog.
                    They share a similar structure and have the same method names info() and make_sound().

                    There is no common superclass or linked the classes together in any way.
                    Even then, we can pack these two different objects into a tuple and
                    iterate through it using a common animal variable. It is possible due to polymorphism.

            Polymorphism and Inheritance

                The child classes in Python inherit methods and attributes from the parent class.
                We can redefine certain methods and attributes specifically to fit the child class,
                which is known as METHOD OVERRIDING.

                Polymorphism allows us to access these overridden methods and attributes
                that have the same name as the parent class.

                    Example 4: Method Overriding

                        from math import pi

                        class Shape:
                            def __init__(self, name):
                                self.name = name

                            def area(self):
                                pass

                            def fact(self):
                                return "I am a two-dimensional shape."

                            def __str__(self):
                                return self.name


                        class Square(Shape):
                            def __init__(self, length):
                                super().__init__("Square")
                                self.length = length

                            def area(self):
                                return self.length**2

                            def fact(self):
                                return "Squares have each angle equal to 90 degrees."


                        class Circle(Shape):
                            def __init__(self, radius):
                                super().__init__("Circle")
                                self.radius = radius

                            def area(self):
                                return pi*self.radius**2

                        a = Square(4)
                        b = Circle(7)
                        print(b)
                        print(b.fact())
                        print(a.fact())
                        print(b.area())

                        Output

                            Circle
                            I am a two-dimensional shape.
                            Squares have each angle equal to 90 degrees.
                            153.93804002589985

                        Here, we can see that the methods such as __str__(), which have
                        not been overridden in the child classes, are used from the parent class.

                Due to polymorphism, the Python interpreter automatically recognizes that the fact() method
                for object a(Square class) is overridden. So, it uses the one defined in the child class.

                On the other hand, since the fact() method for object b isn't overridden,
                it is used from the Parent Shape class.

                NOTE: METHOD OVERLOADING, A WAY TO CREATE MULTIPLE METHODS WITH THE SAME NAME BUT DIFFERENT ARGUMENTS, IS NOT POSSIBLE IN PYTHON.