def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    
    for i in range(n):
        answer.append(s//n)
        s -= s//n
        n -= 1
    
    
    return answer