n = int(input())
money = list(map(int, input().split()))
m = int(input())

def binary_search(start, end):
    global result
    if start > end:
        return result

    mid = (start + end) // 2
    temp = 0
    for i in money:
        if i < mid:
            temp += i
        else:
            temp += mid

    if temp <= m :
        result = max(result, mid)
        return binary_search(mid+1, end)
    else:
        return binary_search(start, mid-1)


if sum(money) <= m:
    print(max(money))
else:
    result = 0
    print(binary_search(1, max(money)))