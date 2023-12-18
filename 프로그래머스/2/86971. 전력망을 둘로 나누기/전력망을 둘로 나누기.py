import math
import sys   
sys.setrecursionlimit(10**6)
def solution(n, wires):
    result = []
    graph = [[] for i in range(n+1)] 
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    for x,y in wires:
        graph[x].remove(y)
        graph[y].remove(x)
        a = (dfs(graph,x,[]))
        b = (dfs(graph,y,[]))
        result.append(abs(a-b))
        graph[x].append(y)
        graph[y].append(x)
        
    return min(result)

def dfs(graph, root, visited):
    count = 1
    visited.append(root)
    for n in graph[root]:
        if n not in visited:
            count += dfs(graph, n, visited)
    return count