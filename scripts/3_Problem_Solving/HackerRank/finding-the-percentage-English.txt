if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

lst=student_marks.get(query_name)
sm=0
for i in lst:
    sm+=i
avg=sm/len(lst)
#print(avg)
print('{:.2f}'.format(avg))

