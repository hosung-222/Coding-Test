n,l = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
for i in range(n):
    check = True
    same_count = 1
    step = [0] * n
    for j in range(1, n):
        #같은경우
        if graph[i][j] == graph[i][j-1]:
            same_count += 1
        # 1칸 높아지는 경우
        elif graph[i][j] -1 == graph[i][j-1]:
            if same_count >= l:
                for k in range(l):
                    if step[j-1-k] == 1:
                        check = False
                        break
                    else:
                        step[j-1-k] = 1
            else:
                check = False
                break
        
        # 1칸 낮아지는 경우
        elif graph[i][j-1] == graph[i][j]+1:
            for k in range(l):
                if j+k < n:
                    if graph[i][j+k] != graph[i][j]:
                        check = False
                        break
                    else:
                        step[j+k] = 1
                else:
                    check = False
                    break
            same_count = 1

        else:
            check = False

    if check == True:
        result += 1

for j in range(n):
    check = True
    same_count = 1
    step = [0] * n
    for i in range(1, n):
        #같은경우
        if graph[i][j] == graph[i-1][j]:
            same_count += 1

        # 1칸 높아지는 경우
        elif graph[i][j] -1 == graph[i-1][j]:
            if same_count >= l:
                for k in range(l):
                    if step[i-1-k] == 1:
                        check = False
                        break
                    else:
                        step[i-1-k] = 1
            else:
                check = False
                break
        
        # 1칸 낮아지는 경우
        elif graph[i-1][j] == graph[i][j]+1:
            for k in range(l):
                if i+k < n:
                    if graph[i+k][j] != graph[i][j]:
                        check = False
                        break
                    else:
                        step[i+k] = 1
                else:
                    check = False
                    break
            same_count = 1
        
        else:
            check = False

    if check == True:
        result += 1

print(result)