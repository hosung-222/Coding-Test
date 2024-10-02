import heapq
import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0 and heap:
        print(heapq.heappop(heap))
    elif x == 0:
        print(0)
    else:
        heapq.heappush(heap, x)