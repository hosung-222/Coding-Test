from collections import Counter
def solution(topping):
    cnt =0 
    dic = Counter(topping)
    s = set()
    for i in topping:
        dic[i] -= 1
        s.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(s):
            cnt += 1
            
    return cnt
