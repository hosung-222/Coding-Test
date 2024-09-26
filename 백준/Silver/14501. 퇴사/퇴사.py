n = int(input())  
day = [] 
for i in range(n):
    t, p = map(int, input().split())  # 상담에 걸리는 시간 t, 받을 수 있는 돈 p
    day.append((t, p))

dp = [0] * (n + 1)  

# 모든 날짜에 대해 상담을 선택하거나 선택하지 않는 방식으로 최대 수익 계산
for i in range(n):
    time, pay = day[i] 
    # 상담이 끝나는 날짜가 퇴사일을 넘지 않으면 상담을 진행할 수 있음
    if i + time <= n:
        dp[i + time] = max(dp[i + time], dp[i] + pay)

    # 그날 상담을 하지 않는 경우, 다음날로 최대 수익을 넘김
    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[n])
