n = int(input())
data = list(map(int, input().split()))
x = int(input())

data.sort()

result = 0
start = 0
end = n-1
for i in range(n):
    while start < end:
        if data[start] + data[end] > x:
            end -= 1
        elif data[start] + data[end] < x:
            start += 1
        else:
            start += 1
            end -= 1
            result += 1

print(result)