from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    start_x, start_y = None, None
    lever_x, lever_y = None, None
    end_x, end_y = None, None
    
    for i in range(len(maps)):
        if "S" in maps[i]:
            start_x, start_y = i, maps[i].index("S")
        if "L" in maps[i]:
            lever_x, lever_y = i, maps[i].index("L")
        if "E" in maps[i]:
            end_x, end_y = i, maps[i].index("E")

    to_lever = bfs(start_x, start_y, lever_x, lever_y, maps)
    to_end = bfs(lever_x, lever_y, end_x, end_y, maps)
    
    if to_lever == -1 or to_end == -1:
        return -1
    else:
        return to_lever + to_end

def bfs(start_x, start_y, end_x, end_y, maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((start_x, start_y, 0))
    visited[start_x][start_y] = True
    
    while q:
        x, y, distance = q.popleft()
        if x == end_x and y == end_y:
            return distance
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X" and not visited[nx][ny]:
                q.append((nx, ny, distance + 1))
                visited[nx][ny] = True
                
    return -1
    