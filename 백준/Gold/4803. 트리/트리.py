def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

case = 0
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n+1)]
    cycle = set()
    result = 0

    # 간선 정보 입력 받기
    for _ in range(m):
        a, b = map(int, input().split())
        parent_a = find_parent(parent, a)
        parent_b = find_parent(parent, b)
        if parent_a != parent_b:
            union_parent(parent, parent_a, parent_b)
        else:
            cycle.add(parent_a)

    # 모든 노드의 부모 갱신
    for i in range(1, n+1):
        find_parent(parent, i)

    # 그룹 확인
    group = set()
    for cycle_vertex in cycle:
        group.add(parent[cycle_vertex])

    for i in range(1, n+1):
        if parent[i] in group:
            continue
        result += 1
        group.add(parent[i])

    case += 1
    if result == 0:
        print("Case %d: No trees." % case)
    elif result == 1:
        print("Case %d: There is one tree." % case)
    else:
        print("Case %d: A forest of %d trees." % (case, result))
