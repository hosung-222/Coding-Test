from collections import deque
def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(distance[x])
            break
        for i in (x-1, x+1, x*2):
            if 0<= i <= 10**5 and not distance[i]:
                distance[i] = distance[x] + 1
                q.append(i)

n, k = map(int, input().split())
distance = [0] * (10**5+1)
bfs()