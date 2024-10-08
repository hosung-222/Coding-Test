import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()
start = 0
end = n - 1
min_sum = float('inf') 
result_x, result_y = 0, 0

while start < end:
    sum_value = data[start] + data[end]
    if abs(sum_value) < abs(min_sum):
        result_x = start
        result_y = end
        min_sum = sum_value
    
    if sum_value == 0:
        result_x = start
        result_y = end
        break
    
    elif sum_value > 0:
        end -= 1
    else:
        start += 1

print(data[result_x], data[result_y])