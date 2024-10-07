h, w = map(int, input().split())
block = list(map(int, input().split()))

left_h = [0] * w
right_h = [0] * w

left_h[0] = block[0]
for i in range(1, w):
    left_h[i] = max(left_h[i-1], block[i])

right_h[w-1] = block[w-1]
for i in range(w-2, -1, -1):
    right_h[i] = max(right_h[i+1], block[i])

result = 0
for i in range(1, w-1):
    water = min(left_h[i], right_h[i]) - block[i]
    if water > 0:
        result += water

print(result)