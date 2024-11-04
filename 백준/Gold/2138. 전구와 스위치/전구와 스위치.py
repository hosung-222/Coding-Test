def toggle(arr, count):
    for i in range(1, n-1):
        if arr[i-1] != goal[i-1]:
            count += 1
            for j in range(i-1, i+2):
                arr[j] = not arr[j]
    if arr[n-1] != goal[n-1]:
        count += 1
        arr[n-1] = not arr[n-1]
        arr[n-2] = not arr[n-2]
    if arr == goal:
        return count
    else: return -1

n = int(input())
switch = list(map(int, input().strip()))
goal = list(map(int, input().strip()))

if switch == goal:
    print(0)
else:
    copy_list = switch.copy()
    copy_list[0] = not switch[0]
    copy_list[1] = not switch[1]
    count = toggle(switch, 0)
    if count != -1:
        print(count)
    else:
        count = toggle(copy_list, 1)
        print(count)
        
   