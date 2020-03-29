# Python Miscellaneous

    Python Generators

        What are generators in Python?

            There is a lot of overhead in building an iterator in Python;
            Implementation a class with __iter__() and __next__() method, keep track of internal states,
            raise StopIteration when there was no values to be returned etc.


            Python generators are a simple way of creating iterators.
            All the overhead we mentioned above are automatically handled by generators in Python.

            Simply speaking, a generator is a function that returns an object (iterator) which
            we can iterate over (one value at a time).

        How to create a generator in Python?

            It is like defining a normal function with yield statement instead of a return statement.

            If a function contains at least one yield statement
            (it may contain other yield or return statements), it becomes a generator function.
            Both yield and return will return some value from a function.

            The difference is that,
            while A RETURN STATEMENT TERMINATES A FUNCTION ENTIRELY,
            YIELD STATEMENT PAUSES THE FUNCTION SAVING ALL ITS STATES AND LATER CONTINUES FROM THERE ON SUCCESSIVE CALLS.

        Differences between Generator function and a Normal function

            Generator function contains one or more yield statement.
            When called, it returns an object (iterator) but does not start execution immediately.
            Methods like __iter__() and __next__() are implemented automatically.
                So we can iterate through the items using next().
            Once the function yields, the function is paused and the control is transferred to the caller.
            Local variables and their states are remembered between successive calls.
            Finally, when the function terminates, StopIteration is raised automatically on further calls.

            Note: One final thing to note is that we can use generators with for loops directly.

            This is because, a for loop takes an iterator and iterates over it using next() function.
            It automatically ends when StopIteration is raised.

        Python Generator Expression
            Simple generators can be easily created on the fly using generator expressions.
            It makes building generators easy.

            Same as lambda function creates an anonymous function,
            generator expression creates an anonymous generator function.

            The syntax for generator expression is similar to that of a list comprehension in Python.
            But the square brackets are replaced with round parentheses.

            The major difference between a list comprehension and a generator expression is that
            while list comprehension produces the entire list, generator expression produces one item at a time.

            They are kind of lazy, producing items only when asked for.
            For this reason, a generator expression is much more memory efficient 
            than an equivalent list comprehension.


        Why generators are used in Python?
            There are several reasons which make generators an attractive implementation to go for.

            1. Easy to Implement
                Generators can be implemented in a clear and concise way as compared to their iterator class.
                Following is an example to implement a sequence of power of 2's using iterator class.

                    class PowTwo:
                        def __init__(self, max = 0):
                            self.max = max

                        def __iter__(self):
                            self.n = 0
                            return self

                        def __next__(self):
                            if self.n > self.max:
                                raise StopIteration

                            result = 2 ** self.n
                            self.n += 1
                            return result

                This was lengthy. Now lets do the same using a generator function.

                    def PowTwoGen(max = 0):
                        n = 0
                        while n < max:
                            yield 2 ** n
                            n += 1

                Since, generators keep track of details automatically.

            2. Memory Efficient
                A normal function to return a sequence will create the entire sequence in memory before 
                returning the result. This is an overkill if the number of items in the sequence is very large.

                Generator implementation of such sequence is memory friendly and 
                is preferred since it only produces one item at a time.

            3. Represent Infinite Stream
                Generators are excellent medium to represent an infinite stream of data. 
                Infinite streams cannot be stored in memory and since generators produce only one item at a time, 
                it can represent infinite stream of data.

                The following example can generate all the even numbers (at least in theory).

                    def all_even():
                        n = 0
                        while True:
                            yield n
                            n += 2

            4. Pipelining Generators
            Generators can be used to pipeline a series of operations. This is best illustrated using an example.

            Suppose we have a log file from a famous fast food chain. The log file has a column (4th column) 
            that keeps track of the number of pizza sold every hour and we want to sum it to find the total 
            pizzas sold in 5 years.

            Assume everything is in string and numbers that are not available are marked as 'N/A'.
            A generator implementation of this could be as follows.

                with open('sells.log') as file:
                    pizza_col = (line[3] for line in file)
                    per_hour = (int(x) for x in pizza_col if x != 'N/A')
                    print("Total pizzas sold = ",sum(per_hour))