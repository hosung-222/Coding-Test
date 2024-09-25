import math
n = int(input()) # 시험장 개수
room = list(map(int, input().split()))
b, c = map(int, input().split()) #b: 총감독관 감시 c:부감독관 감시

cnt = 0
for r in room:
    cnt += 1
    temp = r - b
    if temp > 0:
        cnt += math.ceil(temp / c)

print(cnt)