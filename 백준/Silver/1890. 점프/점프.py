n = int(input())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

def jump():
    for i in range(n):
        for j in range(n):
            temp = board[i][j]
            if temp == 0 or dp[i][j] == 0:
                continue
            if i + temp < n:
                dp[i + temp][j] += dp[i][j]
            if j + temp < n:
                dp[i][j + temp] += dp[i][j]
    return dp[n-1][n-1]

print(jump())