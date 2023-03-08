def solution(n):
    cnt = 0
    for i in range(n,0,-1):
        s = 0
        for j in range(i,0,-1):
            s += j
            if s > n:
                break
            elif s == n:
                cnt += 1
                break
            
    return cnt
                