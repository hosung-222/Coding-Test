n = int(input())
data = []

for _ in range(n):
    l, h = map(int, input().split())
    data.append((l, h))

data.sort(key=lambda x: x[0])

max_h = max(data, key=lambda x: x[1])[1]
max_idx = next(i for i, x in enumerate(data) if x[1] == max_h)

height = data[0][1]
result = 0
for i in range(max_idx):
    result += (data[i+1][0] - data[i][0]) * height
    if height < data[i+1][1]:
        height = data[i+1][1]

result += max_h

height = data[-1][1]
for i in range(n-1, max_idx, -1):
    result += (data[i][0] - data[i-1][0]) * height
    if height < data[i-1][1]:
        height = data[i-1][1]

print(result)