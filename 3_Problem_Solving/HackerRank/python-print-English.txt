if __name__ == '__main__':
    n = int(input())
a=[]
for i in range(n):
    j=i+1
    a.append(str(j))
print(''.join(a))

# Alternate way
print(*range(1,N+1), sep='')
