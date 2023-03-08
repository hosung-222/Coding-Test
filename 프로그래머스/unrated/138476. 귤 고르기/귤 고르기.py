from collections import deque
def solution(k, tangerine):
    tangerine.sort()
    dic = {}
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    cnt = deque(sorted(dic.items(), key = lambda x:x[1]))
    
    x = len(tangerine)
    while x > k:
        x -= cnt[0][1]
        cnt.popleft()
        
    if x!= k:
        return len(cnt) + 1
    else:
        return len(cnt)
        