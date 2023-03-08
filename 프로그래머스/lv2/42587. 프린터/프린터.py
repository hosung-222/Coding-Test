from collections import deque
def solution(priorities, location):
    answer = 0
    que = deque([x,i] for i, x in enumerate(priorities))
    
    while len(que):
        item = que.popleft()
        if que and item[0] < max(que)[0]:
            que.append(item)
        else:
            answer += 1
            if item[1] == location:
                return answer

            
        
            
    
        
    