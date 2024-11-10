n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0
for i in range(n):
    start = 0
    end = n-2
    exclude_arr = arr[:i] + arr[i+1:]
    while start < end:
        temp = exclude_arr[start] + exclude_arr[end]
        if temp == arr[i]:
            result += 1
            break

        elif temp > arr[i]:
            end -= 1
        elif temp < arr[i]:
            start += 1

print(result)