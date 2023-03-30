def solution(x, y, n):
    cnt = 0
    s = set()
    s.add(x)
    while s:
        e = set()
        if y in s:
            return cnt
        for i in s:
            if i+n <= y:
                e.add(i+n)
            if i*2 <= y:
                e.add(i*2)
            if i*3 <= y:
                e.add(i*3)
        s= e
        cnt += 1
        
    return -1
        