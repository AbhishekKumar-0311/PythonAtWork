===================================================================================
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from scipy import stats
a=input()
b=input()

ar=np.array([int(a) for a in b.split()])
print(np.average(ar))
print(np.median(ar))
print(int(stats.mode(ar)[0]))

===================================================================================

from statistics import mean,median,mode
N = int(input().strip())

arr = [int(i) for i in input().strip().split(' ')]
arr.sort()

print('{0:.1f}'.format(sum(arr)/N))

if N % 2 == 1:
    print('{0:.1f}'.format(arr[int((N-1)/2)]))
else:
    print('{0:.1f}'.format(0.5*(arr[int(N/2)-1]+arr[int(N/2)])))
    
counts=[]
for i in arr:
    counts.append(arr.count(i))
if max(counts) > 1:
    print(arr[counts.index(max(counts))])
else:
    print(min(arr))

===================================================================================

import numpy as np;
import statistics;
from collections import Counter;

n = input();
ar = np.asarray(list(map(int, input().split(' '))));
print(statistics.mean(ar));
print(statistics.median(ar));
m = sorted(Counter(ar).most_common(), key=lambda x: x[1] * 10000 - x[0], reverse = True);
print(m[0][0]);

===================================================================================