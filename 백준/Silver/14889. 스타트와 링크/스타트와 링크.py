n = int(input())
ablities = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
result = float(1e9)

def dfs(depth, idx):
    global result
    if depth == n//2:
        team1, team2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    team1 += ablities[i][j]
                elif not visited[i] and not visited[j]:
                    team2 += ablities[i][j]
        result = min(result, abs(team1-team2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

dfs(0,0)
print(result)