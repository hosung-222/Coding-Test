from collections import deque
import copy
mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
    [[0,1,2,3]]
]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
result = int(1e9)
cctv = []
for i in range(n):
    for j in range(m):
        if room[i][j] != 0  and room[i][j] != 6:
            cctv.append((room[i][j], i, j))
    
def fill(room, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx<0 or nx >= n or ny<0 or ny>=m:
                break
            if room[nx][ny] == 6:
                break
            if room[nx][ny] == 0:
                room[nx][ny] = -1

def dfs(depth, room):
    global result
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += room[i].count(0)
        result = min(result, count)
        return

    tmp_room = copy.deepcopy(room)
    number, x, y = cctv[depth]
    for i in mode[number]:
        fill(tmp_room, i, x, y)
        dfs(depth+1, tmp_room)
        tmp_room = copy.deepcopy(room)

dfs(0, room)
print(result)

