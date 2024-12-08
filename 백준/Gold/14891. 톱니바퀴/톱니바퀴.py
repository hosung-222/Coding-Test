from collections import deque
wheels = [deque(list(map(int, input()))) for _ in range(4)]

def to_left(idx, direction):
    if idx <0:
        return
    if wheels[idx][2] != wheels[idx+1][6]:
        to_left(idx-1, -direction)
        wheels[idx].rotate(direction)

def to_right(idx, direction):
    if idx > 3:
        return
    if wheels[idx][6] != wheels[idx-1][2]:
        to_right(idx+1, -direction)
        wheels[idx].rotate(direction)
    
k = int(input())
for i in range(k):
    idx, direction = map(int, input().split())
    idx -= 1
    to_right(idx+1, -direction)
    to_left(idx-1, -direction)
    wheels[idx].rotate(direction)

score = 0
for i in range(4):
    if wheels[i][0] == 1:
        score += 2**i

print(score)