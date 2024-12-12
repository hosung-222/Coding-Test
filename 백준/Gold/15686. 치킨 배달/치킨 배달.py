def calculate_distance():
    city_distance = 0
    for h in house:
        temp_distance = int(1e9)
        for s in chose:
            distance = abs(s[0]-h[0]) + abs(s[1]-h[1])
            temp_distance = min(temp_distance, distance)
        city_distance += temp_distance
    return city_distance


def dfs(depth, start):
    global result 
    if M == len(chose):
        result = min(result, calculate_distance())
        return
    for i in range(start, len(store)):
        chose.append(store[i])
        dfs(depth+1, i+1)
        chose.pop()
        
        
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
result = int(1e9)
store = []
house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            store.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))

chose = []
dfs(0, 0)

print(result)