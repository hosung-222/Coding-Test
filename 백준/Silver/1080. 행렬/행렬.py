n, m = map(int, input().split())
count = 0
li = []
for i in range(2):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input())))
    li.append(temp)

for i in range(n-2):
    for j in range(m-2):
        if li[0][i][j] != li[1][i][j]:
            count += 1
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if li[0][x][y] == 0:
                        li[0][x][y] = 1
                    else:
                        li[0][x][y] = 0

if li[0] == li[1]:
    print(count)
else:
    print(-1)