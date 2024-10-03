from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]
result = [[-1] * m for _ in range(n)]

start_x, start_y = 0, 0
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 2:
            start_x, start_y = i, j
            break

q = deque()
q.append((start_x, start_y))
result[start_x][start_y] = 0

while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if result[nx][ny] == -1 and mapp[nx][ny] == 1:
            result[nx][ny] = result[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 0:
            result[i][j] = 0

for row in result:
    print(' '.join(map(str, row)))
