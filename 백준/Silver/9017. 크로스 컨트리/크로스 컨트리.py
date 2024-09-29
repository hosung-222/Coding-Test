from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    teams = list(map(int, input().split()))
    team_count = defaultdict(int)
    team_score = defaultdict(list)

    for team in teams:
        team_count[team] += 1

    rank = 0
    for team in teams:
        if team_count[team] == 6:
            rank += 1
            team_score[team].append(rank)
    
    print(min(team_score, key=lambda x: (sum(team_score[x][:4]), team_score[x][4], team_score[x][5])))