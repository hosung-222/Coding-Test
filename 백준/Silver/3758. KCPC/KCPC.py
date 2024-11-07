T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())
    teams = [[0]*k for _ in range(n)]
    push_count = [0] * n
    last_push = [0] * n

    for log in range(m):
        i, j, s = map(int, input().split())
        teams[i-1][j-1] = max(teams[i-1][j-1], s)
        push_count[i-1] += 1
        last_push[i-1] = log
    
    team_score = []
    for idx in range(n):
        total_socre = sum(teams[idx])
        team_score.append((total_socre, push_count[idx], last_push[idx], idx+1))

    team_score.sort(key=lambda x: (-x[0], x[1], x[2]))

    for rank, (score, push_count, last_push, team_id) in enumerate(team_score, start=1):
        if team_id == t:
            print(rank)
            break
