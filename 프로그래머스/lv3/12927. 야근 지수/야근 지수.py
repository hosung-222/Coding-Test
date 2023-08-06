import heapq
def solution(n, works):
    heap = []
    for i in works:
        heapq.heappush(heap, (-i, i))
    answer = 0
    while n:
        x = heapq.heappop(heap)[1]
        x -= 1
        heapq.heappush(heap, (-x , x))
        n -= 1
    
    for w in heap:
        if w[1] < 0:
            return 0
        answer += w[1] ** 2
    return answer