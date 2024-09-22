n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))


result = 0
min_price = price[0]

for i in range(n-1):
    result += min_price * distance[i]

    if min_price > price[i+1]:
        min_price = price[i+1]
print(result)