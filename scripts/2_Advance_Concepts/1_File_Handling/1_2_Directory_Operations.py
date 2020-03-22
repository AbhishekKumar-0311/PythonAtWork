# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 00:43:53 2020

@author: abhi0
"""

# OS Methods
import os
os.name
os.getcwd()
print(os.getcwd())
os.stat(os.getcwd())

# os.access() function in the standard library to check whether a file exists
# and is accessible at the same time.
os.access('fh_test.md', os.F_OK)

# listdir() - To list the directory contents
import os
entries = os.listdir('E:\SpyderProjects')
print(entries)
print(os.listdir('E:\SpyderProjects'))

# To print the directory contents line by line
entries = os.listdir(os.getcwd())
for entry in entries:
    print(entry)

# s.scandir() returns an iterator as opposed to a list
# ScandirIterator points to all the entries in the current directory.
# We can loop over the contents of the iterator and print out the filenames
entries = os.scandir(os.getcwd())
print(type(entries)) # Output : <class 'nt.ScandirIterator'> 
for entry in entries:
    print(entry.name)

# Same as above
with os.scandir(os.getcwd()) as entries:
    for entry in entries:
        print(entry.name)

# To change the directory        
os.chdir('E:\\')
print(os.getcwd())

# Takes in the path of the new directory. If the full path is not specified,
# the new directory is created in the current working directory
os.mkdir('test') # Create
os.chdir('E:\\test') # Change to new directory
print(os.getcwd()) # Check the current directory

# To Rename the directory
os.chdir('E:\\')
os.mkdir('test_2') # Create
os.rename('test_2','new_one')

# File can be removed (deleted) using the remove() method.
# rmdir() removes an empty directory
os.chdir('E:\SpyderProjects')
os.remove('E:\\SpyderProjects\tet.txt')
os.listdir()

os.rmdir('new_one')
os.listdir()

# rmtree() method inside the shutil module : use the rmtree() method inside the shutil module

