n = int(input())
m = int(input())
place = list(map(int, input().split()))

max_h = 0
max_h = max(max_h, place[0])

for i in range(m - 1):
    d = place[i + 1] - place[i]
    h = (d + 1) // 2  
    max_h = max(max_h, h)

max_h = max(max_h, n - place[-1])
print(max_h)
