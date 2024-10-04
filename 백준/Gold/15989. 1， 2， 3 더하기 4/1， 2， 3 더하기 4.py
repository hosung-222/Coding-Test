t = int(input())
test_case = [int(input()) for _ in range(t)]
max_n = max(test_case)

dp = [0] * (max_n+1)
numbers = [1, 2, 3]
dp[0] = 1

for num in numbers:
    for i in range(num, max_n+1):
        dp[i] += dp[i-num]

for t in test_case:
    print(dp[t])
