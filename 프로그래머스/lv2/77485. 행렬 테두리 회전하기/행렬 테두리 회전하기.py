def solution(rows, columns, queries):
    arr = [[c for c in range(r*columns+1, (r+1)*columns+1)] for r in range(rows)]
    result = []
    
    for q in queries:
        q = [x-1 for x in q]
        tmp = arr[q[0]][q[1]]
        mini = tmp
        
        for i in range(q[0]+1, q[2]+1):
            arr[i-1][q[1]] = arr[i][q[1]]
            mini = min(mini, arr[i][q[1]])
            
        for i in range(q[1]+1, q[3]+1):
            arr[q[2]][i-1] = arr[q[2]][i]
            mini = min(mini, arr[q[2]][i])
            
        for i in range(q[2]-1, q[0]-1, -1):
            arr[i+1][q[3]] = arr[i][q[3]]
            mini = min(mini, arr[i][q[3]])
            
        for i in range(q[3]-1, q[1]-1, -1):
            arr[q[0]][i+1] = arr[q[0]][i]
            mini = min(mini, arr[q[0]][i])
        arr[q[0]][q[1]+1] = tmp
        result.append(mini)
        
    return result