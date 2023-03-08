def solution(clothes):
    dic = {}
    for n, c in clothes:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    cnt = 1
    for i in dic.keys():
        cnt *= (1 + dic[i])
    
    return cnt-1