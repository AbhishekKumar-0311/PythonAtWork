
===================================================================================

import numpy as np

m=map(int,input().split())

n=np.array([ int(x) for x in input().split(' ')])
m=np.array([ int(x) for x in input().split(' ')])

o = np.dot(n,m)/np.sum(m)

print(o)

===================================================================================
non numpy sol
===================================================================================


a=int(input())

m=[ int(x) for x in input().split(' ')]
n=[ int(x) for x in input().split(' ')]
#print(m)
#print(n)
o = []
for i in range(len(m)):
    o.append(m[i]*n[i])
#print(o)
k=sum(o)
j=sum(n)
print(float(round(k/j,1)))

===================================================================================
non numpy sol
===================================================================================

N = map(int,input().split())
X = list(map(int, input().strip().split(' ')))
W = list(map(int, input().strip().split(' ')))
sum_X = sum([a*b for a,b in zip(X,W)])
print(round((sum_X/sum(W)),1))