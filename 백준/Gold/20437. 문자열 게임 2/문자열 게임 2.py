from collections import defaultdict

def find_length(w, k):
    indices = defaultdict(list)

    for idx, char in enumerate(w):
        indices[char].append(idx)
    
    min_length = float('inf')
    max_length = 0

    for v in indices.values():
        if len(v) >= k:
            for i in range(len(v) -k + 1):
                 length = v[i+k-1] - v[i] + 1
                 min_length = min(min_length, length)
                 max_length = max(max_length, length)
    
    if min_length == float('inf'):
        return -1
    else:
        return min_length, max_length
            


t = int(input())
for _ in range(t):
    w = input()
    k = int(input())

    result = find_length(w, k)
    if result == -1:
        print(-1)
    else:
        print(result[0], result[1])

