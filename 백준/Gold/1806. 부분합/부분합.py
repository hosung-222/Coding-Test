n, s = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, 0
temp_sum = 0
min_length = float('inf') 

while end < n:
    # 부분합이 s보다 작으면 end를 증가시키면서 부분합을 늘린다
    temp_sum += data[end]
    end += 1
    
    # 부분합이 s 이상이면, 그 구간의 길이를 확인하고 start를 증가시키면서 최소 길이 갱신
    while temp_sum >= s:
        min_length = min(min_length, end - start)
        temp_sum -= data[start]
        start += 1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)