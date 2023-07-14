from collections import deque
def solution(maps):
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    result = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    def dfs(x,y):
        q = deque()
        q.append((x,y))
        sum = 0
        while q:
            x,y = q.pop()
            if not visited[x][y]:
                sum += int(maps[x][y])
                visited[x][y] = True
                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if 0<= nx < len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny] !="X":
                        q.append((nx,ny))
                
        return sum
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and visited[i][j] == False:
                day = dfs(i,j)
                result.append(day)
    
                
    return sorted(result) if result else [-1]
                