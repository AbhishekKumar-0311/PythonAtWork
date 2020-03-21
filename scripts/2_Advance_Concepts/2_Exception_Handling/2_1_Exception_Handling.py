# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:39:39 2020

@author: abhi0
"""
import errno
import os

# Raise an Exception
# The program comes to a halt and 
# displays our exception to screen, offering clues about what went wrong
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# If this condition turns out to be True, the program can continue.
# If the condition turns out to be False, the program throws an AssertionError exception
import sys
assert ('linux' in sys.platform), "This code runs on Linux only."


# Exception Handling with single except
try: 
	f = open('fh_tet.md') 
except (FileNotFoundError, PermissionError):
    print("File not found or Permission denied")

# OSError is a base class that’s common to 
# both the FileNotFoundError and PermissionError exceptions.    
try: 
	f = open('fh_tet.md')
except OSError:
    print("OS Error - BaseClass")

# Create situations where multiple except clauses might match
try:
	f = open('fh_tet.md')
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('Permission Denied') 
except IOError:
    print('File is not accessible')
except OSError:
    print("OS error")

# Using OSError to produce error    no(errno) and error string(strerror) 
try:
	f = open('fh_tet.md')
except OSError as exception:
    print(exception)

# Using OSError (base class) to produce error no
try:
	f = open('fh_tet.md')
except OSError as e:
    print(e,'\n',e.strerror,'\n',e.errno )
	# 'No such file or directory'
    if e.errno == 13:
        print(e.strerror)
        print("this will print")
    # 'No such file or directory'
    if e.errno == 2:
        print(e.strerror)

# Try and Except, Else and Finally block
try:
    fp = open("fh_test.md")
except PermissionError:
    print("some default data")
else:
    print(fp.seek(9))
    print(fp.tell())
    print(fp.read())
# This clause is executed no matter what, and is generally used to release external resources.
finally:
   fp.close()    


# To view the full range of errors (1)
print({i: os.strerror(i) for i in sorted(errno.errorcode)})

# To get entire list of error string (2)
for i in errno.errorcode:
    print(os.strerror(i), i)

''' Print test '''
a=9
b=8
print('sim is',a+b,'difis',a-b,'a=',a)
print('sim is'+ '(a+b)' + 'difis'+ '(a-b)' + 'a=' + '(a)')

'''
try:
	f = open('fh_tet.md')
except OSError as e:
    # 'No such file or directory'
    if e.errno == errno.ENOENT:
        print(e.strerror)
        print("No such file or directory")
        # handle one way
    elif e.errno == errno.EPERM:
        print(e.strerror)
        print("Permission not granted")
    elif e.errno == errno.EBADF:
        print(e.strerror)
        print("Bad file descriptor")
        # handle another way
'''
        


