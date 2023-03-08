def solution(citations):
    maxd = [0]
    for i in range(len(citations)//2, len(citations)+1):
        pcnt = 0
        mcnt = 0
        for j in citations:
            if i <= j:
                pcnt += 1
            else:
                mcnt += 1
        if pcnt >= i and i >= mcnt:
            maxd.append(i)
    return max(maxd)
    
        
            