# Python Overview

Python Variables, Constants and Literals

    Python Variables

        A variable is a named location used to store data in the memory.

            number = 10
            number = 1.1
        Initially, the value of number was 10. Later it's changed to 1.1.

        Note: In Python, we don't assign values to the variables,
        whereas Python gives the reference of the object (value) to the variable.

        Note : Python is a type inferred language; it can automatically know datatype.

    Constants

        A constant is a type of variable whose value cannot be changed.

        In Python, constants are usually declared and assigned on a module.
        Here, the module means a new file containing variables, functions etc which is imported to main file.
        Inside the module, constants are written in all capital letters and underscores separating the words.

        Example : Declaring and assigning value to a constant
            Create a constant.py

            PI = 3.14
            GRAVITY = 9.8
            Create a main.py

            import constant

            print(constant.PI)
            print(constant.GRAVITY)

            When you run the program, the output will be:
            3.14
            9.8

        In the above program, we create a constant.py module file.
        Then, we assign the constant value to PI and GRAVITY.
        After that, we create a main.py file and import the constant module.

        Note: In reality, we don't use constants in Python.
        The globals or constants module is used throughout the Python programs.

        Rules and Naming Convention for Variables and constants
            Constant and variable names should have a combination of letters in lowercase (a to z)
            or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
            For example:
                snake_case
                MACRO_CASE
                camelCase
                CapWords
            Create a name that makes sense. For example, vowel makes more sense than v.
            If you want to create a variable name having two words, use underscore to separate them.
            For example:
                my_name
                current_salary
            Use capital letters possible to declare a constant.
            For example:
                PI
                G
                MASS
                SPEED_OF_LIGHT
                TEMP
            Never use special symbols like !, @, #, $, %, etc.
            Don't start a variable name with a digit.

    Literals
        Literal is a raw data given in a variable or constant.
        There are various types of literals they are as follows:

        Numeric Literals
            Numeric Literals are immutable (unchangeable).
            Numeric literals can belong to 3 different numerical types Integer, Float, and Complex.

        String literals
            A string literal is a sequence of characters surrounded by quotes.
            We can use both single, double or triple quotes for a string.
            And, a character literal is a single character surrounded by single or double quotes.

        Boolean literals
            A Boolean literal can have any of the two values: True or False.

        Special literals
            Python contains one special literal i.e. None. We use it to specify to that field that is not created.

        Literal Collections
            There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.
