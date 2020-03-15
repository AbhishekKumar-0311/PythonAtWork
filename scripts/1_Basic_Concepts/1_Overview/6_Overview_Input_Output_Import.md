# Python Overview

Python Input, Output and Import

    Python provides numerous built-in functions : available to us at the Python prompt.

    Some of the functions like input() and print() are widely used for standard input and output
    operations respectively.

    Python Output Using print() function
    We use the print() function to output data to the standard output device (screen).

    We can also output data to a file.
    The actual syntax of the print() function is

        print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
        Here, objects is the value(s) to be printed.

    The sep separator is used between the values. It defaults into a space character.
    After all values are printed, end is printed. It defaults into a new line.

    The file is the object where the values are printed and its default value is sys.stdout (screen).

    Output formatting

        This can be done by using the str.format() method. This method is visible to any string object.

            >>> x = 5; y = 10
            >>> print('The value of x is {} and y is {}'.format(x,y))
            The value of x is 5 and y is 10

        Here the curly braces {} are used as placeholders.
        We can specify the order in which it is printed by using numbers (tuple index).

        We can even use keyword arguments to format the string.

            >>> print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
            Hello John, Goodmorning

        We can even format strings like the old sprintf() style used in C programming language.
        We use the % operator to accomplish this.

            >>> x = 12.3456789
            >>> print('The value of x is %3.2f' %x)
            The value of x is 12.35
            >>> print('The value of x is %3.4f' %x)
            The value of x is 12.3457

    Python Input

        In Python, we have the input() function to take the input from the user.
        The syntax for input() :
            input([prompt])
            where prompt is the string we wish to display on the screen and is optional.

                >>> num = input('Enter a number: ')
                Enter a number: 10
                >>> num
                '10'

            Here, we can see that the entered value 10 is a string, not a number.

            To convert this into a number we can use int() or float() functions.
                >>> int('10')
                10
                >>> float('10')
                10.0
                This same operation can be performed using the eval() function.

            It can evaluate even expressions, provided the input is a string
                >>> int('2+3')
                Traceback (most recent call last):
                File "<string>", line 301, in runcode
                File "<interactive input>", line 1, in <module>
                ValueError: invalid literal for int() with base 10: '2+3'
                >>> eval('2+3')
                5

    Python Import

        When the program grows bigger, it is a good idea to break it into different modules.

        A module is a file containing Python definitions and statements.
        Python modules have a filename and end with the extension .py.

        Definitions inside a module can be imported to another module or the interactive interpreter in Python.
        We use the import keyword to do this.

            >>> from math import pi
            >>> pi
            3.141592653589793

        While importing a module, Python looks at several places defined in sys.path.
        It is a list of directory locations.

            >>> import sys
            >>> sys.path
            ['',
            'C:\\Python33\\Lib\\idlelib',
            'C:\\Windows\\system32\\python33.zip',
            'C:\\Python33\\DLLs',
            'C:\\Python33\\lib',
            'C:\\Python33',
            'C:\\Python33\\lib\\site-packages']

        We can add our own location to this list as well.