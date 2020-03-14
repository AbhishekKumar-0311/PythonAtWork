# Python Overview

Python Statement, Indentation and Comments

    Python Statement

        Instructions that a Python interpreter can execute are called statements.
        For example, a = 1 is an assignment statement. Others are if statement, for statement, while statement etc.

        Multi-line statement
            In Python, end of a statement is marked by a newline character.
            But it can be extended over multiple lines with the line continuation character (\).
                For example:

                    a = 1 + 2 + 3 + \
                        4 + 5 + 6 + \
                        7 + 8 + 9

                This is explicit line continuation.

            In Python, line continuation is implied inside parentheses ( ), brackets [ ] and braces { }.
                For instance, we can implement the above multi-line statement as

                    a = (1 + 2 + 3 +
                        4 + 5 + 6 +
                        7 + 8 + 9)

                Here, the surrounding parentheses ( ) do the line continuation implicitly.
                Same is the case with [ ] and { }.
                For example:

                    colors = ['red',
                            'blue',
                            'green']

            We could also put multiple statements in a single line using semicolons, as follows

                a = 1; b = 2; c = 3

    Python Indentation

        Most of the programming languages like C, C++, Java use braces { } to define a block of code.
        Python uses indentation.

        A code block (body of a function, loop etc.) starts with indentation and ends with the first unindented line.
        The amount of indentation is up to you, but it must be consistent throughout that block.

        Generally four whitespaces are used for indentation and is preferred over tabs.


        Indentation can be ignored in line continuation. But it's a good idea to always indent. It makes the code more readable.
            For example:

                if True:
                    print('Hello')
                    a = 5
            and

                if True: print('Hello'); a = 5

            both are valid and do the same thing. But the former style is clearer and better.

            Incorrect indentation will result into IndentationError.

    Python Comments

        It describes what's going on inside a program.
        Hash (#) symbol is used to start writing a comment.
        It extends up to the newline character.
        Python Interpreter ignores comment.
            For example:
                #This is a comment
                #print out Hello
                print('Hello')

        Multi-line comments

            For comments that extend multiple lines, hash (#) is used at the beginning of each line.
                For example:

                    #This is a long comment
                    #and it extends
                    #to multiple lines

            Another way of doing this is to use triple quotes, either ''' or """.

            These triple quotes are generally used for multi-line strings but can be used as multi-line comment as well.
            Unless they are not docstrings, they do not generate any extra code.
                For example:

                    """This is also a
                    perfect example of
                    multi-line comments"""

    Docstring in Python
        Docstring is short for documentation string.

        It is a string that occurs as the first statement in a module, function, class, or method definition.
        We must write what a function/class does in the docstring.

        Triple quotes are used while writing docstrings.
        Docstring is available to us as the attribute __doc__ of the function.

            >>> print(double.__doc__)