from collections import deque

n, k = map(int, input().split())

def bfs(n, k):
    max_limit = 100001
    dist = [-1] * max_limit
    dist[n] = 0
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            return dist[k]

        if x * 2 < max_limit and dist[x*2] == -1:
            dist[x*2] = dist[x]
            q.appendleft(x*2)
        
        if x -1 >=0 and dist[x-1] == -1:
            dist[x-1] = dist[x] + 1
            q.append(x-1)
        
        if x + 1 < max_limit and dist[x+1] == -1:
            dist[x+1] = dist[x] + 1
            q.append(x+1)

    return -1

print(bfs(n, k))