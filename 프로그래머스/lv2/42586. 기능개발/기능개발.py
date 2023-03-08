def solution(progresses, speeds):
    day = []
    answer = []
    for i in range(len(progresses)):
        x = (100- progresses[i]) // speeds[i]
        if (100- progresses[i]) % speeds[i] != 0:
            x += 1
        day.append(x)
        
    cnt = 1
    process = day[0]
    for i in day[1:]:
        if process >= i:
            cnt += 1
        else:
            process = i
            answer.append(cnt)
            cnt = 1
            
    answer.append(cnt)
            
    return answer
        