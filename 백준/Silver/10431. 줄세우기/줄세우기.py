def bubble_sort(c, arr):
    cnt = 0
    for i in range(len(arr)-1, 0 , -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt += 1
    print(c, cnt)

p = int(input())
for t in range(p):
    students = list(map(int, input().split()))
    bubble_sort(students[0], students[1:])
