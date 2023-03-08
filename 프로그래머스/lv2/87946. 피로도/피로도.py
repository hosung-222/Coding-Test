import itertools
def solution(k, dungeons):
    x = list(itertools.permutations(dungeons,len(dungeons)))
    answer = []
    for i in x:
        start = k
        cnt = 0
        for a, b in i:
            if start>= a:
                start -= b
                cnt += 1
        
        answer.append(cnt)
    
    return max(answer)