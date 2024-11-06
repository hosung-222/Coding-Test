import heapq
test_case = 1
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(n, maze):
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = maze[0][0]
    q = [(maze[0][0], 0, 0)]

    while q:
        dist, x, y = heapq.heappop(q)

        if dist > distance[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                cost = dist + maze[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    return distance[n-1][n-1]

while True:
    n = int(input())
    if n == 0:
        break
    maze = [list(map(int, input().split())) for _ in range(n)]
    min_cost = dijkstra(n, maze)
    
    print("Problem " + str(test_case) + ": " + str(min_cost))
    test_case += 1