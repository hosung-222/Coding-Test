n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
result = 0

list_a.sort()
list_b.sort(reverse=True)

for i in range(n):
    result += list_a[i] * list_b[i]
    
print(result)
    