led = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1]   # 9
]

# 두 숫자 간의 LED 차이를 사전에 계산하여 저장
led_diff = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        for k in range(7):
            if led[i][k] != led[j][k]:
                led_diff[i][j] += 1

# 입력 받기
N, K, P, X = map(int, input().split())

current_floor = str(X).zfill(K)
result = 0

# 가능한 1부터 N까지의 층수에 대해 확인
for target_floor in range(1, N + 1):
    target_str = str(target_floor).zfill(K)
    
    total_diff = 0
    for i in range(K):
        total_diff += led_diff[int(current_floor[i])][int(target_str[i])]
        if total_diff > P:
            break
    
    # 반전한 LED 수가 P 이하일 경우 카운트
    if 0 < total_diff <= P:
        result += 1

print(result)