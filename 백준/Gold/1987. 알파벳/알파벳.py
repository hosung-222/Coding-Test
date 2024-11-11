from sys import setrecursionlimit
from collections import defaultdict
setrecursionlimit(100000)  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
max_count = 0

memo = defaultdict(int)

def dfs(x, y, count, visited):
    global max_count
    if memo[(x, y, visited)] >= count:
        return  

    memo[(x, y, visited)] = count
    max_count = max(max_count, count)
    
    # 4방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            next_char = board[nx][ny]
            bit = 1 << (ord(next_char) - ord('A'))

            if not (visited & bit): 
                dfs(nx, ny, count + 1, visited | bit)  

initial_bit = 1 << (ord(board[0][0]) - ord('A'))
dfs(0, 0, 1, initial_bit)

print(max_count)