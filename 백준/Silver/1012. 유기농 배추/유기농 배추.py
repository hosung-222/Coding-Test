from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    land = [[0]*m for _ in range(n)]
    result = 0
    for i in range(k):
        x, y = map(int, input().split())
        land[y][x] = 1

    visit = [[0]*m for _ in range(n)]
    for a in range(n):
        for b in range(m):
            if land[a][b] == 1 and visit[a][b] == 0:
                visit[a][b] = 1
                result += 1
                q = deque()
                q.append((a, b))
                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if land[nx][ny] == 1 and visit[nx][ny] == 0:
                            visit[nx][ny] = 1
                            q.append((nx, ny))

    print(result)
