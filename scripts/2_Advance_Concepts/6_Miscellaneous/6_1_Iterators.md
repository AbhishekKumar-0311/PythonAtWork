# Python Miscellaneous

    Python Iterators

        What are iterators in Python?

            Iterators are objects that can be iterated upon.
			An object which will return data, one element at a time.
            They are implemented within for loops, comprehensions, generators etc. but hien in plain sight.

            Python iterator object must implement two special methods,
                __iter__() and __next__(), collectively called the iterator protocol.

            Most of built-in containers in Python like: list, tuple, string etc. are iterables.

            The iter() function (which in turn calls the __iter__() method) returns an iterator from them.

        Iterating Through an Iterator in Python

            next() function - to manually iterate through all the items of an iterator.
            When we reach the end and there is no more data to be returned, it will raise StopIteration.

            We can iterate over any object that can return an iterator, for example list, string, file etc.

            >>> for element in my_list:
            ...     print(element)
            ...
            4
            7
            0
            3

        How for loop actually works?

            The for loop is able to iterate automatically through the list.
            In fact the for loop can iterate over any iterable.

                for element in iterable:
                    # do something with element
                Is actually implemented as.

                # create an iterator object from that iterable
                iter_obj = iter(iterable)

                # infinite loop
                while True:
                    try:
                        # get the next item
                        element = next(iter_obj)
                        # do something with element
                    except StopIteration:
                        # if StopIteration is raised, break from loop
                        break

            So internally, the for loop creates an iterator object, iter_obj by calling iter() on the iterable.

            This for loop is actually an infinite while loop.

            Inside the loop, it calls next() to get the next element and executes the body of the for loop with
            this value. After all the items exhaust, StopIteration is raised which is internally caught and the
            loop ends. Note that any other kind of exception will pass through.

        Building Own Iterator in Python

            We just have to implement the methods __iter__() and __next__().

            The __iter__() method returns the iterator object itself.
            The __next__() method must return the next item in the sequence.
            On reaching the end, and in subsequent calls, it must raise StopIteration.

            Here, we show an example that will give us next power of 2 in each iteration. Power exponent starts from zero up to a user set number.

                class PowTwo:
                    """Class to implement an iterator
                    of powers of two"""

                    def __init__(self, max = 0):
                        self.max = max

                    def __iter__(self):
                        self.n = 0
                        return self

                    def __next__(self):
                        if self.n <= self.max:
                            result = 2 ** self.n
                            self.n += 1
                            return result
                        else:
                            raise StopIteration

            Now we can create an iterator and iterate through it as follows.

                >>> a = PowTwo(4)
                >>> i = iter(a)
                >>> next(i)
                1
                >>> next(i)
                2
                >>> next(i)
                4
                >>> next(i)
                8
                >>> next(i)
                16
                >>> next(i)
                Traceback (most recent call last):
                ...
                StopIteration
                We can also use a for loop to iterate over our iterator class.

                >>> for i in PowTwo(5):
                ...     print(i)
                ...
                1
                2
                4
                8
                16
                32

        Python Infinite Iterators

            It is not necessary that the item in an iterator object has to exhaust. 
			There can be infinite iterators (which never ends). We must be careful when handling such iterator.

        There's an easier way to create iterators in Python. To learn more visit: Python generators using yield.