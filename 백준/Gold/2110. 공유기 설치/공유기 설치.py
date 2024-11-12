n, c= map(int, input().split())
houses = []
result = 0

for i in range(n):
    houses.append(int(input()))

houses.sort()
def binary_search(arr, start, end):
    while start <= end:
        mid = (start+end)// 2
        current = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                count += 1
                current = arr[i]
        
        if count >= c:
            global result
            start = mid + 1
            result  = mid
        else:
            end = mid -1

binary_search(houses, 1, houses[-1]-houses[0])
print(result)