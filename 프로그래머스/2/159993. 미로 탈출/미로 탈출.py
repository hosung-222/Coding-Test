from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, start_x, start_y, end_x, end_y):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((start_x, start_y, 0))
    visited[start_x][start_y] = True

    while queue:
        x, y, distance = queue.popleft()

        if x == end_x and y == end_y:
            return distance
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))

    return -1

def solution(maps):
    lever_x, lever_y = None, None
    start_x, start_y = None, None
    exit_x, exit_y = None, None
    
    n = len(maps)
    m = len(maps[0])

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'L':
                lever_x, lever_y = i, j
            elif maps[i][j] == 'S':
                start_x, start_y = i, j
            elif maps[i][j] == 'E':
                exit_x, exit_y = i, j
    

    lever_distance = bfs(maps, start_x, start_y, lever_x, lever_y)
    exit_distance = bfs(maps, lever_x, lever_y, exit_x, exit_y)
    
    if lever_distance == -1 or exit_distance == -1:
        return -1
    return lever_distance + exit_distance