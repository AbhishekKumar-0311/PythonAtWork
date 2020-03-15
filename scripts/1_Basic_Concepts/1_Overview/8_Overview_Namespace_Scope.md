# Python Overview

Python Namespace and Scope

    What is Name in Python?
        Name (also called identifier) is simply a name given to objects.
        Everything in Python is an object. Name is a way to access the underlying object.

        For example, when we do the assignment a = 2,
        here 2 is an object stored in memory and a is the name we associate it with.
        We can get the address (in RAM) of some object through the built-in function, id().

            >>> a = 5
            >>> a = 'Hello World!'
            >>> a = [1,2,3]

        All these are valid and a will refer to three different types of object at different instances.
        Functions are objects too, so a name can refer to them as well.

        Our same name a can refer to a function and we can call the function through it, pretty neat.

    What is a Namespace in Python?
        So now that we understand what names are, we can move on to the concept of namespaces.

        To simply put it, namespace is a collection of names.

        In Python, you can imagine a namespace as a mapping of every name, you have defined, to corresponding objects.

        Different namespaces can co-exist at a given time but are completely isolated.

        A namespace containing all the built-in names is created when we start the
        Python interpreter and exists as long we don't exit.

        This is the reason that built-in functions like id(), print() etc. are always available
        to us from any part of the program. Each module creates its own global namespace.

        These different namespaces are isolated.
        Hence, the same name that may exist in different modules do not collide.

        Modules can have various functions and classes. A local namespace is created when a function is called,
        which has all the names defined in it. Similar, is the case with class.

        Python Variable Scope
            Although there are various unique namespaces defined, we may not be able to access all of them from every part of the program. The concept of scope comes into play.

            Scope is the portion of the program from where a namespace can be accessed directly without any prefix.

            At any given moment, there are at least three nested scopes.

            Scope of the current function which has local names
            Scope of the module which has global names
            Outermost scope which has built-in names
            When a reference is made inside a function, the name is searched in the local namespace,
            then in the global namespace and finally in the built-in namespace.



