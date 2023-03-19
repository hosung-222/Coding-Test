from collections import deque
def solution(n, m, section):
    q = deque(section)
    cnt = 0
    end = 0
    while q: 
        start = q.popleft()
        if start > end:
            cnt += 1
            end = start + m - 1
    return cnt
        