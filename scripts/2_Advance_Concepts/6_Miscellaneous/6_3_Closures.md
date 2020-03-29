# Python Miscellaneous

    Python Closures

        Nonlocal variable in a nested function

            Before getting into what a closure is, we have to first understand
            what a nested function and nonlocal variable is.

            A function defined inside another function is called a nested function.
            Nested functions can access variables of the enclosing scope.

            In Python, these non-local variables are read only by default and
            we must declare them explicitly as non-local (using nonlocal keyword) in order to modify them.

            Following is an example of a nested function accessing a non-local variable.

                def print_msg(msg):
                # This is the outer enclosing function

                    def printer():
                # This is the nested function
                        print(msg)

                    printer()

                # We execute the function
                # Output: Hello
                print_msg("Hello")

            We can see that the nested function printer() was able to
            access the non-local variable msg of the enclosing function.

        Defining a Closure Function

            In the example above, what would happen if the last line of the function print_msg()
            returned the printer() function instead of calling it? This means the function was defined as follows.

                def print_msg(msg):
                # This is the outer enclosing function

                    def printer():
                # This is the nested function
                        print(msg)

                    return printer  # this got changed

                # Now let's try calling this function.
                # Output: Hello
                another = print_msg("Hello")
                another()

            That's unusual.


            The print_msg() function was called with the string "Hello" and
            the returned function was bound to the name another.
            On calling another(), the message was still remembered although we had
            already finished executing the print_msg() function.

            This technique by which some data ("Hello") gets attached to the code is called CLOSURE IN PYTHON.

            This value in the enclosing scope is remembered even when the
            variable goes out of scope or the function itself is removed from the current namespace.

            Try running the following in the Python shell to see the output.

                >>> del print_msg
                >>> another()
                Hello
                >>> print_msg("Hello")
                Traceback (most recent call last):
                ...
                NameError: name 'print_msg' is not defined

        When do we have a closure?

            The criteria that must be met to create closure in Python are summarized in the following points.

                We must have a nested function (function inside a function).
                The nested function must refer to a value defined in the enclosing function.
                The enclosing function must return the nested function.

            When to use closures?
            So what are closures good for?

                Closures can avoid the use of global values and provides some form of data hiding.
                It can also provide an object oriented solution to the problem.

                When there are few methods (one method in most cases) to be implemented in a class,
                closures can provide an alternate and more elegant solutions.
                But when the number of attributes and methods get larger, better implement a class.

                Here is a simple example where a closure might be more preferable than
                defining a class and making objects. But the preference is all yours.

                All function objects have a __closure__ attribute that returns a tuple of cell objects
                if it is a closure function. Referring to the example above,
                we know times3 and times5 are closure functions.

                    >>> make_multiplier_of.__closure__
                    >>> times3.__closure__
                    (<cell at 0x0000000002D155B8: int object at 0x000000001E39B6E0>,)
                    The cell object has the attribute cell_contents which stores the closed value.

                    >>> times3.__closure__[0].cell_contents
                    3
                    >>> times5.__closure__[0].cell_contents
                    5