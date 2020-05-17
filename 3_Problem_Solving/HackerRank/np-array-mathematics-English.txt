

===================================================================================

n, _= map(int,input().split())

a= np.array([input().split() for _ in range(n) ],int)
b= np.array([input().split() for _ in range(n) ],int)

#print(a)
#print(b)

print( a + b)
print( a - b)
print( a * b)
# print( a / b) # Return the values in decimals
print( a // b) # return rounded
print( a % b)
print( a**b)

print( np.add(a, b))
print( np.subtract(a, b))
print( np.multiply(a, b))
print( np.divide(a, b))
print( np.mod(a, b))
print( np.power(a, b))


===================================================================================