
===================================================================================

import numpy as np

a = np.array(list(map(float,input().split())),float)

# print(a)
np.set_printoptions(sign=' ')
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))

===================================================================================

import numpy

A = numpy.array([float(i) for i in input().strip().split()])

numpy.set_printoptions(sign=' ')
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))


===================================================================================
