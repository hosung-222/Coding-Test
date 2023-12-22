def solution(storey):
    answer = 0
    queue = list(map(int, str(storey)))
    while(queue):
        p = queue.pop()
        if (p == 5 and ((queue and queue[-1] < 5) or not queue)) or p < 5:
            answer += p
        else:
            answer += 10 - p
            if(queue):
                queue.append(queue.pop() + 1) #올림
            else:
                answer += 1
    
    return answer