def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)

    if a>b:
        parents[a] = b
    else:
        parents[b] = a

n = int(input())
m = int(input())

cities = []
parents = [i for i in range(n+1)]
for i in range(n):
    cities.append(list(map(int, input().split())))
    for j in range(n):
        if cities[i][j] == 1:
            union(parents, i+1, j+1)

plan = list(map(int, input().split()))
set_plan = set(plan)


check = find(parents, plan[0])
for i in set_plan:
    if find(parents, i) != check:
        print("NO")
        exit(0)
print("YES")

