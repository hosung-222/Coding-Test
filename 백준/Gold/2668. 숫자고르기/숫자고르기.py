n = int(input())
graph = [[] for _ in range(n+1)]
result = set()

for i in range(1, n+1):
    graph[int(input())].append(i)

for i in range(1, n+1):
    visited = [False] * (n+1)
    stack = [i]
    visited[i] = True

    while stack:
        v = stack.pop()
        for j in graph[v]:
            if not visited[j]:
                stack.append(j)
                visited[j] = True

            elif i == j:
                result.add(j)

result = list(result)
result.sort()
print(len(result))
for i in result:
    print(i)
