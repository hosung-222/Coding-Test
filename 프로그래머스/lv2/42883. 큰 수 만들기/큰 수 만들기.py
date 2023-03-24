from collections import deque
def solution(number, k):
    n = deque(number)
    q = deque(n.popleft())
    while n and k:
        if q:
            if q[-1] < n[0]:
                q.pop()
                k -= 1
            else:
                q.append(n.popleft())
        else:
            q.append(n.popleft())
    if k:
        q.pop()
        
    for i in n:
        q.append(i)
        
    return ''.join(q)