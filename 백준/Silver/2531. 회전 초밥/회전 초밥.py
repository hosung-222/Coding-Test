from collections import defaultdict
n, d, k, c = map(int, input().split())
sushi = [] 
for i in range(n):
    sushi.append(int(input()))

count = defaultdict(int)
unique_sushi = 0

for i in range(k):
    if count[sushi[i]] == 0:
        unique_sushi += 1
    count[sushi[i]] += 1
max_length = unique_sushi + (1 if count[c]==0 else 0)

for i in range(1, n):
    if count[sushi[(i+k-1)%n]] == 0:
        unique_sushi += 1
    count[sushi[(i+k-1)%n]] += 1

    count[sushi[i-1]] -= 1
    if count[sushi[i-1]] == 0:
        unique_sushi -= 1
    
    max_length = max(max_length, unique_sushi + (1 if count[c] == 0 else 0))

print(max_length)