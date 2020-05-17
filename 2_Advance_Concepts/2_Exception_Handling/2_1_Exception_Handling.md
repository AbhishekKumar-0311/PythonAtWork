# Python Exception Handling

Python Exception Handling

    What are exceptions in Python?

        Python has many built-in exceptions which forces your program to output an error
        when something in it goes wrong.

        When these exceptions occur, it causes the current process to stop
        and passes it to the calling process until it is handled., else it will Crash

        For example, if function A calls function B which in turn calls function C and
        an exception occurs in function C. If it is not handled in C, the exception passes to B and then to A.

        If never handled, an error message is spit out and our program come to a sudden, unexpected halt.

    Catching Exceptions in Python

        A critical operation which can raise exception is placed inside the try clause
        and the code that handles exception is written in except clause.

        For example.

            # import module sys to get the type of exception
            import sys

            randomList = ['a', 0, 2]

            for entry in randomList:
                try:
                    print("The entry is", entry)
                    r = 1/int(entry)
                    break
                except:
                    print("Oops!",sys.exc_info()[0],"occured.")
                    print("Next entry.")
                    print()
            print("The reciprocal of",entry,"is",r)

        Output

            The entry is a
            Oops! <class 'ValueError'> occured.
            Next entry.

            The entry is 0
            Oops! <class 'ZeroDivisionError' > occured.
            Next entry.

            The entry is 2
            The reciprocal of 2 is 0.5

        In this program, we loop until the user enters an integer that has a valid reciprocal. The portion that can cause exception is placed inside try block.

        If no exception occurs, except block is skipped and normal flow continues. But if any exception occurs, it is caught by the except block.

        Here, we print the name of the exception using ex_info() function inside sys module and ask the user to try again. We can see that the values 'a' and '1.3' causes ValueError and '0' causes ZeroDivisionError.

    Catching Specific Exceptions in Python

        In the above example, we did not mention any exception in the except clause.
        A good programming practice is to catch different exceptions and handle every case in different way.
        try:
        # do something
        pass

        except ValueError:
        # handle ValueError exception
        pass

        except (TypeError, ZeroDivisionError):
        # handle multiple exceptions
        # TypeError and ZeroDivisionError
        pass

        except:
        # handle all other exceptions
        pass

    Raising Exceptions

        Exceptions are raised when corresponding errors occur at run time,
        but we can forcefully raise it using the keyword raise.

        We can also optionally pass in value to the exception to clarify why that exception was raised.

            >>> raise KeyboardInterrupt
            Traceback (most recent call last):
            ...
            KeyboardInterrupt

            >>> raise MemoryError("This is an argument")
            Traceback (most recent call last):
            ...
            MemoryError: This is an argument

            >>> try:
            ...     a = int(input("Enter a positive integer: "))
            ...     if a <= 0:
            ...         raise ValueError("That is not a positive number!")
            ... except ValueError as ve:
            ...     print(ve)
            ...
            Enter a positive integer: -2
            That is not a positive number!

    try...finally

        Optional finally clause. This clause is executed no matter what,
        and is generally used to release external resources.

        For example

            try:
            f = open("test.txt",encoding = 'utf-8')
            # perform file operations
            finally:
            f.close()

        This (FINALLY) makes sure the file is closed even if an exception occurs.