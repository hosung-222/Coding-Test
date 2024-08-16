import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    dist = y-x
    temp = 0
    result = 0
    moving = 0

    while temp < dist:
        result += 1
        if result % 2 !=0:
            moving += 1
        temp += moving

    print(result)