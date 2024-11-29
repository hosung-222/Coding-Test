import sys
sys.setrecursionlimit(1 << 25)
def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

def union(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root != v_root:
        if size[u_root] < size[v_root]:
            parent[u_root] = v_root
            size[v_root] += size[u_root]
        else:
            parent[v_root] = u_root
            size[u_root] += size[v_root]

n, q = map(int, sys.stdin.readline().split())
edges = []
for _ in range(n - 1):
    p, node, r = map(int, sys.stdin.readline().split())
    edges.append((r, p, node)) 

queries = []
for i in range(q):
    k, v = map(int, sys.stdin.readline().split())
    queries.append((k, v, i)) 

edges.sort(reverse=True)
queries.sort(reverse=True)

parent = [i for i in range(n + 1)]
size = [1] * (n + 1)

result = [0] * q
edge_idx = 0
for k_value, v_node, idx in queries:
    # 현재 K 값 이상인 간선을 유니온 파인드에 추가
    while edge_idx < len(edges) and edges[edge_idx][0] >= k_value:
        usado_value, u_node, v_node_edge = edges[edge_idx]
        union(u_node, v_node_edge)
        edge_idx += 1
    root_v = find(v_node)
    result[idx] = size[root_v] - 1  # 시작 노드를 제외한 연결된 노드의 수

for res in result:
    print(res)