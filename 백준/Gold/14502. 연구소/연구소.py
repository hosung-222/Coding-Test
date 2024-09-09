from collections import deque
from itertools import combinations
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
empty_spaces = [] # 빈칸 위치
virus_positions = [] # 바이러스 위치

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_spaces.append((i, j))  # 빈 칸 위치 저장
        elif graph[i][j] == 2:
            virus_positions.append((i, j))  # 바이러스 위치 저장

def bfs(temp_graph):
    q = deque(virus_positions) 
    while q:
        x, y = q.popleft()
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2  # 바이러스 퍼짐
                q.append((nx, ny))

def calculate_safe_zone(temp_graph):
    safe_zone = 0
    for i in range(n):
        safe_zone += temp_graph[i].count(0)  # 안전 구역(0)의 개수 세기
    return safe_zone

# 벽 3개를 세우는 모든 조합에 대해 시뮬레이션 실행
max_safe_zone = 0
for walls in combinations(empty_spaces, 3):  # 빈 칸 중에서 3개를 선택
    temp_graph = [row[:] for row in graph]  # 원본 그래프를 복사

    # 선택된 3개의 빈 칸에 벽을 세우기
    for wx, wy in walls:
        temp_graph[wx][wy] = 1
    # 바이러스 확산
    bfs(temp_graph)
    # 안전 구역 계산
    max_safe_zone = max(max_safe_zone, calculate_safe_zone(temp_graph))
print(max_safe_zone)