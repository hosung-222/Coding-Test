def solution(n, k):
    cnt = 0
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)  #몫, 나머지
        rev_base += str(mod)
    x = rev_base[::-1] 
    
    arr = x.split('0')
    for i in arr:
        if i and check(int(i)):
            cnt += 1
    return cnt

def check(n):
    if n == 1:
        return False
    for i in range(2,int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True