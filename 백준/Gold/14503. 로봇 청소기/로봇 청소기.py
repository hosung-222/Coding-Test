from collections import deque

dx = [[-1, 0], [0, 1], [1, 0], [0, -1]]
n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
result = 0
visited = [[0]*m for _ in range(n)]

q = deque()
q.append((r, c))
result += 1
visited[r][c] = 1
while q:
    r, c = q.popleft()
    flag = 0

    for _ in range(4):
        d = (d+3) % 4
        nr = r + dx[d][0]
        nc = c + dx[d][1]
        if 0 <= nr < n and 0<= nc < m and not room[nr][nc]:
            if not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
                result += 1
                flag = 1
                break

    if flag == 0:
        if room[r -dx[d][0]][c-dx[d][1]] != 1:
            q.append((r-dx[d][0], c-dx[d][1]))
        
        else:
            print(result)
            break