import heapq
def solution(operations):
    answer = []
    q = []
    for  s in operations:
        if s[0] == "I" :
            heapq.heappush(q, int(s[2:]))
        elif s[0] == "D":
            if q:
                if s[2:] == "1":
                    q.remove(max(q))
                else:
                    heapq.heappop(q)
    
    if q:
        return (max(q), min(q))
    else:
        return [0,0]