from collections import deque
import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
volume = list(map(int, input().split()))

visited = [[False] * (m + 1) for _ in range(n + 1)]
q = deque()
q.append(s)
visited[0][s] = True
result = -1

for i in range(n):
    for _ in range(len(q)):
        now_volume = q.popleft()
        
        if 0 <= now_volume + volume[i] <= m and not visited[i + 1][now_volume + volume[i]]:
            visited[i + 1][now_volume + volume[i]] = True
            q.append(now_volume + volume[i])
        
        if 0 <= now_volume - volume[i] <= m and not visited[i + 1][now_volume - volume[i]]:
            visited[i + 1][now_volume - volume[i]] = True
            q.append(now_volume - volume[i])

result = -1
for v in range(m, -1, -1):
    if visited[n][v]:
        result = v
        break

print(result)
