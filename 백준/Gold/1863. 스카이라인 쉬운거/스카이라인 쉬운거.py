n = int(input())

skylines = []
for i in range(n):
    x, y = map(int, input().split())
    skylines.append(y)
skylines.append(0)

stack = [0]
count = 0
for y in skylines:
    height = y
    while stack[-1] > y:
        if stack[-1] != height:
            count += 1
            height = stack[-1]
        stack.pop()
    stack.append(y)

print(count)
