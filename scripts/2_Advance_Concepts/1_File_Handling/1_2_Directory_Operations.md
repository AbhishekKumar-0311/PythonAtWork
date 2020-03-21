# Python File Handling

Python Directory and Files Management

    What is Directory in Python?

        A directory or folder is a collection of files and sub directories. Python has the os module, which provides us with many useful methods to work with directories (and files as well).

        Get Current Directory using the getcwd() method.
        Returns the current working directory in the form of a string.

            >>> import os

            >>> os.getcwd()
            'C:\\Program Files\\PyScripter'

        The extra backslash implies escape sequence. The print() function will render this properly.

            >>> print(os.getcwd())
            C:\Program Files\PyScripter

        Changing Directory using the chdir() method.

            The new path that we want to change to must be supplied as a string to this method.
            We can use both forward slash (/) or the backward slash (\) to separate path elements.
            It is safer to use escape sequence when using the backward slash.

                >>> os.chdir('C:\\Python33')

                >>> print(os.getcwd())
                C:\Python33

        List Directories and Files
            All files and sub directories inside a directory can be known using the listdir() method.

            This method takes in a path and returns a list of sub directories and files in that path.
            If no path is specified, it returns from the current working directory.

                >>> print(os.getcwd())
                C:\Python33

        Making a New Directory using the mkdir() method.

            If the full path is not specified, the new directory is created in the current working directory.

                >>> os.mkdir('test')

                >>> os.listdir()
                ['test']

        Renaming a Directory or a File
            The rename() method can rename a directory or a file.
            The first argument is the old name and the new name must be supplies as the second argument.

                >>> os.listdir()
                ['test']

                >>> os.rename('test','new_one')

                >>> os.listdir()
                ['new_one']

        Removing Directory or File
            A file can be removed (deleted) using the remove() method.

            Similarly, the rmdir() method removes an empty directory.

                >>> os.listdir()
                ['new_one', 'old.txt']

                >>> os.remove('old.txt')
                >>> os.listdir()
                ['new_one']

                >>> os.rmdir('new_one')
                >>> os.listdir()
                []

            NOTE : rmdir() method can only remove empty directories.

            To remove a non-empty directory, use the rmtree() method inside the shutil module.