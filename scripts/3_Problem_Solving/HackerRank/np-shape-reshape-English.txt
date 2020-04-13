
===================================================================================
import numpy as np
a=np.array(list(map(int,input().split())))
a.shape=(3,3)
print(a)

===================================================================================

import numpy
tmp = [int(x) for x in input().strip().split()]
arr = numpy.array(tmp)
print(arr.reshape(3, 3))

===================================================================================
import numpy
print numpy.reshape(numpy.array(map(int,raw_input().split())),(3,3))

===================================================================================

import numpy
print(numpy.array(str(raw_input()).strip().split(), int).reshape(3,3))


===================================================================================

A = numpy.array(input().strip().split(),int)
print(numpy.reshape(A,(3,3)))

===================================================================================

import numpy
import sys

for line in sys.stdin:
    my_list = map(int,line.split())
    my_list = numpy.array(my_list)
    my_list.shape = (3,3)
    print my_list

===================================================================================