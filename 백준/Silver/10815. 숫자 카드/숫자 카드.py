n = int(input())
having = list(map(int, input().split()))
result = []
m = int(input())
cards = list(map(int,input().split()))

having.sort()

for card in cards:
    low, high = 0, n-1
    found = False
    while low <= high:
        mid = (low + high) // 2
        if having[mid] < card:
            low = mid + 1
        elif having[mid] > card:
            high = mid - 1
        else:
            result.append(1)
            found = True
            break
    
    if found == False:
        result.append(0)

print(' '.join(map(str, result)))