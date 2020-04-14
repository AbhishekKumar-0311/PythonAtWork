
===================================================================================

import numpy as np

m,_= map(int,input().split())
#print(m)

ar=np.array([input().split() for _ in range(m)],float)
#print(ar)

np.set_printoptions(sign=' ')
print(np.mean(ar,axis=1))
print(np.var(ar,axis=0))
print(round(np.std(ar),12))

===================================================================================



===================================================================================