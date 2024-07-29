from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])
count = 0

for i in a:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) <= len(q) // 2:
                q.append(q.popleft())
                count += 1
            else:
                q.appendleft(q.pop())
                count += 1

print(count)