def solution(n):
    ans = ''
    num = ['1','2','4']
    while n > 0 :
        n -= 1
        ans = num[n%3] + ans
        n //= 3
        
    return ans
    