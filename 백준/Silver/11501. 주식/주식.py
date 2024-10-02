import sys
input = sys.stdin.readline

t =int(input())

for _ in range(t):
    result = 0
    n = int(input())
    stock = list(map(int, input().split()))
    max_price = 0

    for i in range(n-1, -1, -1):
        if stock[i] > max_price:
            max_price = stock[i]
        else:
            result += max_price - stock[i]
    
    print(result)