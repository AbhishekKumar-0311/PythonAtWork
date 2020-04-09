if __name__ == '__main__':
    # x, y, z, n = int(input()), int(input()), int(input()), int(input())
	x, y, z, n = (int(input()) for _ in range(4))
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

# Alternate way
x, y, z, n = (int(raw_input())+1 for _ in range(4))
print [[a,b,c] for a in range(x) for b in range(y) for c in range(z) if a+b+c!=n-1]

'''
for a in range(x+1):

    for b in range(y+1):

        for c in range(z+1):

            if a + b + c != n:
                print(stuff is here)
'''