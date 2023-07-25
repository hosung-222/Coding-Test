from collections import deque
def solution(n, edge):
    answer = 0
    dic = {s:[] for s in range(1, n+1)}
    for s, e in edge:
        dic[s].append(e)
        dic[e].append(s)
    
    distance = [-1]*(n+1)
    
    q = deque([1])
    distance[1] = 0
    
    while q:
        n = q.popleft()
        for i in dic[n]:
            if distance[i] == -1:
                distance[i] = distance[n] + 1
                q.append(i)
    
    return distance.count(max(distance))