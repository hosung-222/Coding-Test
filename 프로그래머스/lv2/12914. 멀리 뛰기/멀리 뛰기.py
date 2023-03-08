def solution(n):
    x = [1] * (n+1)

    for i in range(2,n+1):
        x[i] = ((x[i-1] + x[i-2]) % 1234567)
        
    return x[-1]
        
        