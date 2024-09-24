from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maze[i][j] == "R":
            rx, ry = i, j
        elif maze[i][j] == "B":
            bx, by = i, j

q = deque()
q.append((rx, ry, bx, by, 1))
visited = set()
visited.add((rx, ry, bx, by))

while q:
    rx, ry, bx, by, cnt = q.popleft()
    if cnt > 10:
        print(-1)
        exit()
    for i in range(4):
        nrx, nry, nbx, nby = rx, ry, bx, by
        # 빨간공 움직이기
        while maze[nrx + dx[i]][nry + dy[i]] != "#" and maze[nrx][nry] != "O":
            nrx += dx[i]
            nry += dy[i]
        # 파란공 움직이기
        while maze[nbx + dx[i]][nby + dy[i]] != "#" and maze[nbx][nby] != "O":
            nbx += dx[i]
            nby += dy[i]
        
        # 구멍에 빠진 경우
        if maze[nbx][nby] == "O":
            continue
        if maze[nrx][nry] == "O":
            print(cnt)
            exit()

        # 두 구슬이 같은 위치에 도착하면 위치 조정
        if nrx == nbx and nry == nby:
            # 빨간 공이 더 많이 움직인 경우
            if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): 
                nrx -= dx[i]
                nry -= dy[i]
            # 파란 공이 더 많이 움직인 경우
            else:
                nbx -= dx[i]
                nby -= dy[i]

        # 새로운 상태가 방문되지 않았다면 큐에 추가
        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, cnt + 1))

print(-1)
