from collections import deque
def solution(land):
    n, m = len(land), len(land[0])
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    visit =[[0]*m for _ in range(n)]
    result = [0 for _ in range(m+1)]
    
    def bfs(a,b):
        count = 0
        visit[a][b] = 1
        q = deque()
        q.append((a,b))
        min_oil, max_oil = b, b
    
        while q:
            x, y = q.popleft()
            min_oil = min(y, min_oil)
            max_oil = max(y, max_oil)
            count += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if visit[nx][ny]!= 1 and land[nx][ny] == 1:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
                    
        for i in range(min_oil, max_oil+1):
            result[i] += count

    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and visit[i][j] == 0:
                bfs(i, j)

    return max(result)