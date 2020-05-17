
===================================================================================

import numpy as np

m= int(input())
#print(m)

a=np.array([input().split() for _ in range(m)],int)
b=np.array([input().split() for _ in range(m)],int)
#print(ar)

np.set_printoptions(sign=' ')

print(np.matmul(a,b))

===================================================================================


===================================================================================