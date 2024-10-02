n, k = map(int,input().split())
table = list(input().strip())

result = 0
for i in range(len(table)):
    if table[i] == 'P':
        for j in range(i-k, i+k+1):
            if j >= 0 and j < len(table) and table[j] == 'H':
                table[j] = "N"
                result += 1
                break
print(result)
            

