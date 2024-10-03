from collections import defaultdict
n, d = map(int, input().split())
highway = []
for _ in range(n):
    s, e, l = map(int, input().split())
    if e <= d:  
        highway.append((s, e, l))

dp = [i for i in range(d+1)]

for i in range(d + 1):
    if i > 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)  

    for s, e, l in highway:
        if i == s and e <= d:
            dp[e] = min(dp[e], dp[s] + l)

print(dp[d])