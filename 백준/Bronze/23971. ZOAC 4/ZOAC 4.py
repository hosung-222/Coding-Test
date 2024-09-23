h, w, n , m = map(int, input().split())
x, y = 0, 0

while True:
    h -= 1
    if h < 0:
        break
    x += 1
    h -= n
    if w <= 0:
        break
    

while True:
    w -= 1
    if w < 0:
        break
    y += 1
    w -= m
    if w <= 0:
        break
    

print(x * y)