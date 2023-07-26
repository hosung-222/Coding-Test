from collections import deque
def solution(n, computers):
    answer = 0
    visited = []
    dic = {i:[] for i in range(n)}
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i!=j and computers[i][j] == 1:
                dic[i].append(j)
                
    for i in range(n):
        if i not in visited:
            dfs(i,visited,dic)
            answer += 1
            
    return answer 


def dfs(start,visited, dic):
    q = deque()
    q.append(start)
    while q:
        x = q.pop()
        for i in dic[x]:
            if i not in visited:
                visited.append(i)
                q.append(i)
    
                