from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    result = 0
    if (s1 + s2) % 2 != 0:
        return -1
    
    while s1 != s2:
        if result ==  4*len(queue1):
            return -1
        
        if s1 > s2 :
            x = q1.popleft()
            q2.append(x)
            s1 -= x
            s2 += x
        else : 
            x = q2.popleft()
            q1.append(x)
            s1 += x
            s2 -= x
        result += 1
    return result