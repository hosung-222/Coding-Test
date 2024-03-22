import heapq
def solution(jobs):
    start = -1
    done, answer, now = 0, 0, 0
    heap = []
    
    while done < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1],j[0]])
        
        if heap:
            job = heapq.heappop(heap)
            start = now
            now += job[0]
            answer += now - job[1]
            done += 1
            
        else:
            now += 1
    
    
    return answer // len(jobs)