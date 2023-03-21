from collections import deque
def solution(bridge_length, weight, truck_weights):
    q = [0]* bridge_length
    q = deque(q)
    t = deque(truck_weights)
    q = deque(q)
    time = 0
    total_w = weight
    
    while  q:
        total_w += q.popleft()
        if t and total_w >= t[0]:
            total_w -= t[0]
            q.append(t.popleft())
        elif t:
            q.append(0)
        time += 1
        
    

        
    return time
    
    
        
        
            
        