def solution(name, yearning, photo):
    dic ={}
    result = []
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for i in photo:
        cnt = 0
        for j in i:
            if j in dic:
                cnt += dic[j]
        result.append(cnt)

    return result
    
        