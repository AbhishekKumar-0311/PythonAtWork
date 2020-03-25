# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:14:07 2020

@author: abhi0
"""

st="vibek"
rt=[]
lst=list(st)
l=len(lst)
i=0
while i < l:
    rt.append(lst[l-i-1])
    print('inside loop',rt)
    i+=1
print('ouside',rt)
cst=str(rt)
print(cst)
print(st)


st="vibek"

l=len(st)
i=0
while i < l:
    rt.append(lst[l-i-1])
    print('inside loop',rt)
    i+=1

print('ouside',rt)
cst=''.join(rt)
print(cst)
print(''.join(rt))


