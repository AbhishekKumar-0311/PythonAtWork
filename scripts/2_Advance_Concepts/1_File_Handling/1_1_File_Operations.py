# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:52:23 2020

@author: abhi0
"""

# Open a file
f=open('fh_test.md')
f=open("E:\SpyderProjects\\fh_test.md")

# Python File Methods
#print(f)

# readable() - Returns True if the file stream can be read from
f.readable()

# writable() - Returns True if the file stream can be written to
f.writable()

# seekable() - Returns True if the file stream supports random access
f.seekable()
# To get a integer result 0 or 1
int(f.seekable())

# read() - Read atmost n characters form the file.
# read(5) - Reads till end of file if it is negative or None
f.read()
f.read(5)

# readline() - Read and return ONE LINE from the file.
f.readline()
f.readline(-1)
# readline(5) Reads in at most n bytes from the present line if specified.
f.readline(5)
# Even n is 1700, it only returns a single line 
f.readline(50)

# Read and return a list of LINES from the file.
# Reads in at most n bytes/characters if specified.
f.readlines()
f.readlines(50)

# Returns the current file location
f.tell()

# Change the file position to offset bytes
f.seek(0)
f.seek(9)
# Change the file position to offset bytes, in reference to from 
# (0 = start(by-default), 1=current, 2=end)
f.seek(10,0)
# move two characters ahead from the current position
f.seek(2, 1) #some error
# move to the 3rd character from the end of the file
f.seek(-1,2) #some error 

# Print each line of file
for line in f:
    print(line,end=' ')

# Print each line of file with line number    
for i, line in enumerate(f):
    print(i,line,end=' ')
    if i==10:
        break

# File open with write mode
# NOTE : 'w' mode will overwrite into the file if it already exists.
with open("tet.txt",'w',encoding = 'utf-8') as file:
   file.write("my first file\nThis file\n") # Extra \ is to escape \n
   file.write("This file\n\n")
   file.write("contains three lines\n")
   file.write("contains thirty-three lines\n")
   
   # Write a list of lines to the file.
   file.writelines('lines\n\nHi\nThirdline')

# After writing, try reading it.	
f = open("test.txt")
f.readlines()
file = open("tet.txt")
file.readlines()

# Flush the write buffer of the file stream
file.flush()
# After flushing, nothing can be read even if the file is not yet closed
file.readlines()

# detach() - Separate the underlying binary buffer from the TextIOBase and return it.
file.detach()
# Try reading the file again
# Error message < ValueError: underlying buffer has been detached >
file.readlines()

# fileno() - Return an integer number (file descriptor) of the file.
file.fileno()

# close() - Close an open file. It has no effect if the file is already closed.
f.close()
file.close()


# File Object Attributes
# Open a file with 'f' fd(file descriptor)
filename=f.name
print(filename)
print ("Name of the file: ", f.name)
print ("Closed or not : ", f.closed)
print ("Opening mode : ", f.mode)

# To check whether the file is already open or closed
if not f.closed:
    print('file already open')
else:
    print('file is not yet opened')

# To read series of input files
import fileinput
with fileinput.input(files=('fh_test.md', 'fh_tet.md')) as f:
    for line in f:
        print(line)


