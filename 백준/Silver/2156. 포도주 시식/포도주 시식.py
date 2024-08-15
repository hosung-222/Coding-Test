import sys
input = sys.stdin.readline

n = int(input())
glass = []
for _ in range(n):
    glass.append(int(input()))

result = [0] * n
result[0] = glass[0]

if n>1:
    result[1] = glass[0] + glass[1]

if n > 2:
# 첫번째와 현재 포도주마시기, 두번째와 현재 포도주 마시기, 첫번째와 두번재 포도주 마시기
    result[2] = max(glass[0]+glass[2], glass[1]+glass[2], result[1])

for i in range(3, n):
    # 1. 현재 포도주와 전 포도주를 마시고 전전 포도주를 안마시기
    # 2. 현재 포도주와 전전 포도주를 마시고 전 포도주를 안마시기
    # 3. 전 포도주와 전전 포도주를 마시고 현재 포도주를 안마시기

    result[i] = max((glass[i]+glass[i-1]+result[i-3]), (glass[i]+result[i-2]), (result[i-1]))

print(result[n-1])