if __name__ == '__main__':
    nml=[]
    scl=[]
    for _ in range(int(input())):
        name = input()
        nml.append(name)
        score = float(input())
        scl.append(str(score))
print(type(nml))
print(type(scl))
print(nml)
print(scl)

scl2=scl.copy()
print(scl2)

mx1=min(scl2)
print(mx1)
while min(scl2) == mx1:
    scl2.remove(min(scl2))
mx2=min(scl2)
print(mx2)
'''
a=[]
for i,m in enumerate(scl):
    if m == mx2:
        a.append(nml[i])
        print(a)
a.sort()
'''
c= [n for i,(m,n) in enumerate(zip(scl,nml)) if m==mx2]
print('\n'.join(sorted(c)))

# Alternate way

if __name__ == '__main__':
    marksheet = []
    for _ in range(0,int(input())):
        marksheet.append([input(), float(input())])
    '''
    n = int(input())
    marksheet = [[input(), float(input())] for _ in range(n)]
    '''
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))