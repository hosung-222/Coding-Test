import math
def solution(n, stations, w):
    answer = 0
    idx = 1
    for s in stations:
        answer += math.ceil(((s-w) - idx) / ((w*2)+1))
        idx =  s+w+1
    
    answer += math.ceil((n+1 - idx) / ((w*2)+1))
    
    return answer