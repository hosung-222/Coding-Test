def solution(triangle):
    arr = triangle
    for i in range(1, len(triangle)):
        for j in range(len(arr[i])):
            if j == 0:
                arr[i][j] += arr[i-1][0]
            elif j == len(arr[i])-1 :
                arr[i][j] += arr[i-1][-1]
            else:
                arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
    
    return max(arr[-1])