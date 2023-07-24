room = int(input())
temp = [[0]*room for _ in range(room)]
students = []
dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]
for _ in range(room*room):
    a = list(map(int, input().split()))
    students.append(a)

for s in range(room**2):
    student = students[s]
    arr = []
    for x in range(room):
        for y in range(room):
            if temp[x][y] == 0:
                like = 0
                blank = 0
                for r in range(4): # 주변 칸 탐색
                    nx = dx[r] + x
                    ny = dy[r] + y

                    if 0<=nx<room and 0<=ny<room:
                        if temp[nx][ny] in student[1:]: #좋아하는 사람이 인접한 경우 카운팅
                            like += 1
                        if temp[nx][ny] == 0:  #빈칸이 있는 경우 카운팅
                            blank += 1
                arr.append([like, blank, x, y])
    arr.sort(key=lambda x:(-x[0], -x[1], x[2],x[3]))
    temp[arr[0][2]][arr[0][3]] = student[0]

result = 0
students.sort()
for i in range(room):
    for j in range(room):
        grade = 0 
        for r in range(4):
            nx = dx[r] + i
            ny = dy[r] + j
            if 0<=nx<room and 0<=ny<room:
                if temp[nx][ny] in students[temp[i][j]-1]:
                    grade += 1
        
        if grade != 0:
            result += 10**(grade-1)

print(result)