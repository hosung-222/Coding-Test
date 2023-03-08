def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    a = []
    b = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            a.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            b.append(str2[i]+str2[i+1])
    cnt_all = len(a) + len(b)        
    cntn = 0
    for i in a:
        if i in b:
            cntn += 1
            b.remove(i)
    cnt_all -= cntn
    
    if cnt_all:
        return int(cntn / cnt_all *65536)
    else:
        return 65536
            