from collections import deque

def solution(gems):
    gem_types = len(set(gems)) 
    gem_count = {}
    min_length = len(gems)
    min_range = [0, len(gems) - 1]

    temp = deque()
    start = 0

    for end, gem in enumerate(gems):
        if gem not in gem_count:
            gem_count[gem] = 0
        gem_count[gem] += 1
        temp.append(gem)

        while len(gem_count) == gem_types:
            if end - start < min_length:
                min_length = end - start
                min_range = [start, end]

            gem_count[temp[0]] -= 1
            if gem_count[temp[0]] == 0:
                del gem_count[temp[0]]
            temp.popleft()
            start += 1

    return [min_range[0] + 1, min_range[1] + 1] 