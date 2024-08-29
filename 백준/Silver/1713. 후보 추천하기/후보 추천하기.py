import heapq
import sys
input = sys.stdin.readline

n = int(input())
t = int(input())
data = list(map(int, input().split()))
student = {}

for s in data:
    if s not in student:
        if len(student) >= n:
            a = heapq.nsmallest(min(student), student, key=student.get)
            student.pop(a[0])
        student[s] = 1
    else:
        student[s] += 1

result = []
for h in student.keys():
    result.append(h)
result.sort()
print(*result)