def dfs(row):
    global result
    if row == n:
        result += 1
        return
    for col in range(n):
        if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
            # 퀸을 놓을 수 있는 위치면 배치
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
            dfs(row + 1)
            # 백트래킹: 퀸 제거
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

n = int(input())
result = 0
cols = [False] * n
diag1 = [False] * (2 * n - 1)  # 주대각선
diag2 = [False] * (2 * n - 1)  # 부대각선
dfs(0)
print(result)
