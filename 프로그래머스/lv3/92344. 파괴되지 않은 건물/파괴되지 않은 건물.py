def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    arr = [[0]*(m+1) for _ in range(n+1)]
    for t, r1,c1, r2,c2, d in skill:
        if t == 1:
            degree = -d
        else:
            degree = d
        arr[r1][c1] +=  degree
        arr[r2+1][c1] += -degree
        arr[r1][c2+1] += -degree
        arr[r2+1][c2+1] += degree
    
    for i in range(len(arr)-1):
        for j in range(len(arr[0])-1):
            arr[i][j+1] += arr[i][j]
    
    for j in range(len(arr[0])-1):
        for i in range(len(arr)-1):
            arr[i+1][j] += arr[i][j]
            
    for i in range(n):
        for j in range(m):
            board[i][j] += arr[i][j]
            if board[i][j] > 0:
                answer+= 1
    return answer