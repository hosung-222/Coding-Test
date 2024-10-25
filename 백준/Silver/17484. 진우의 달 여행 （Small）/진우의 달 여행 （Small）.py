INF = float('inf')

n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
dp = [[[INF]*3 for _ in range(m)] for _ in range(n)]

for i in range(m):
    for j in range(3):
        dp[0][i][j] = space[0][i]

dir_moves = [1, 0, -1]
for r in range(1, n):
    for c in range(m):
        for d in range(3):
            c_prev = c - dir_moves[d]
            if 0 <= c_prev < m:
                for d_prev in range(3):
                    if d != d_prev:
                        dp[r][c][d] = min(dp[r][c][d], dp[r-1][c_prev][d_prev] + space[r][c])

min_result = INF
for c in range(m):
    for d in range(3):
        min_result = min(min_result, dp[n-1][c][d])

print(min_result)