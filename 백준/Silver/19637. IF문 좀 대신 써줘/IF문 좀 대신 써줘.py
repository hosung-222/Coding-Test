from bisect import bisect_left
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
validation = []
num_list = []
for _ in range(n):
    title, power = input().split()
    validation.append([title, int(power)])
    num_list.append(int(power))

for _ in range(m):
    score = int(input())
    index = bisect_left(num_list, score)
    print(validation[index][0])
    