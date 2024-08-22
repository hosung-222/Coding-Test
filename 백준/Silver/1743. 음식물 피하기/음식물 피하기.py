from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
n, m, k = map(int, input().split())
trash = set()

for _ in range(k):
    x, y = map(int, input().split())
    trash.add((x-1, y-1))

def bfs(x, y):
    cnt = 0
    q = deque()
    q.append((x, y))
    trash.remove((x, y))  # 방문한 좌표를 trash 집합에서 제거
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in trash:
                q.append((nx, ny))
                trash.remove((nx, ny))  # 방문한 좌표를 즉시 제거
    return cnt

for x, y in list(trash):  # 집합을 순회하면서 bfs 실행
    if (x, y) in trash:
        result = max(result, bfs(x, y))

print(result)
