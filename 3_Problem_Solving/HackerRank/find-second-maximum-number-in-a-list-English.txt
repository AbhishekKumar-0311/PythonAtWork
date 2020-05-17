

i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print max(lis)

# Alternate way

print(max([x for x in arr if x != max(arr)]))
