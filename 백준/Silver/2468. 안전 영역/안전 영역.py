from collections import deque
import sys
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n = int(input())
max_height = 0
land = [list(map(int, input().split())) for _ in range(n)]
max_height = max(max(row) for row in land)

result = []
for t in range(max_height + 1):
    temp = 0
    visited = [[False] * n for _ in range(n)]  

    for i in range(n):
        for j in range(n):
            if land[i][j] > t and not visited[i][j]:
                visited[i][j] = True
                temp +=1
                q = deque()
                q.append((i,j))
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        if land[nx][ny] > t and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx,ny))
    result.append(temp)
if(max(result)<0):
    print(1)
print(max(result))