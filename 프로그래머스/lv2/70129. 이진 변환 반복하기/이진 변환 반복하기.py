def solution(s):
    result = [0,0]
    while s!= '1':
        result[0] += 1
        result[1] += s.count('0')
        s = format(s.count('1'),'b')
        s = str(s)
        
    return result

        
    
        