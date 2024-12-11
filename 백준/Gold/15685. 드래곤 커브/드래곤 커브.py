# 0: x좌표가 증가하는 방향 (→)
# 1: y좌표가 감소하는 방향 (↑)
# 2: x좌표가 감소하는 방향 (←)
# 3: y좌표가 증가하는 방향 (↓)
dx = [1, 0 , -1, 0]
dy = [0, -1, 0, 1]


N = int(input())
board = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    board[x][y] = 1
    temp = [d]
    
    for _ in range(g):
        for i in range(len(temp)-1, -1, -1):
            temp.append((temp[i]+1) % 4)
    
    for i in range(len(temp)):
        x, y = x + dx[temp[i]], y + dy[temp[i]]
        board[x][y] = 1

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            result += 1

print(result)