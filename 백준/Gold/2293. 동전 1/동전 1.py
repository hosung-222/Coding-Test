import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1  # 0원을 만드는 방법은 1가지 (동전 사용하지 않기)

type = []

for _ in range(n):
    t = int(input())
    type.append(t)

for t in range(n):
    coin = type[t]
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])
