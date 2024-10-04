def can_transform(S, T):
    from collections import deque

    visited = set()
    def dfs(current):
        if len(current) < len(S):
            return False
        if current == S:
            return True
        if current in visited:
            return False
        visited.add(current)
        result = False
        if current[-1] == 'A':
            result |= dfs(current[:-1])
        if current[0] == 'B':
            result |= dfs(current[1:][::-1])
        return result

    return 1 if dfs(T) else 0

S = input().strip()
T = input().strip()

print(can_transform(S, T))
