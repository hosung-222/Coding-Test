def solution(s):
    if len(s) % 2 == 0:
        lcnt = 0
        rcnt = 0
        for i in s:
            if lcnt < rcnt :
                return False
            else:
                if i == '(':
                    lcnt += 1
                else:
                    rcnt += 1
        if lcnt == rcnt:
            return True
        else:
            return False
        
    else:
        return False