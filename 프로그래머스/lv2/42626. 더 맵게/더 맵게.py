from heapq import*
def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while True:
        x = heappop(scoville)
        if x < K and len(scoville) <= 0:
            return -1
        
        if x < K:
            heappush(scoville, x+heappop(scoville)*2)
            cnt += 1
        else:
            return cnt
            