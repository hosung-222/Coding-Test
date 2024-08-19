import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
r, c, k = map(int, input().split())

load = []
for _ in range(r):
    load.append(input().strip())

visited = [[False]*c for _ in range(r)]
result = 0

def dfs(x, y, distance):
    global result
    if distance == k and x==0 and y == c-1 :
        result += 1
    else:
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and load[nx][ny] == '.':
                visited[nx][ny] = True
                dfs(nx, ny, distance+1)
                visited[nx][ny] = False

dfs(r-1, 0, 1)
print(result)