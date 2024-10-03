n = int(input())
count = list(map(int, input().split()))

result = [0] * n

for i in range(n):
    space = count[i]
    for j in range(n):
        if result[j] == 0:
            if space == 0:
                result[j] = i+1
                break
            space -= 1


print(" ".join(map(str,result)))