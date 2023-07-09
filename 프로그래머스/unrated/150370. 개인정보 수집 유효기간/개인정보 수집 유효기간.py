def solution(today, terms, privacies):
    dic = {}
    result = []
    for i in terms:
        x = i.split(" ")
        dic[x[0]] = x[1]
    tod = today.split(".")
    ttt = tod[0] + tod[1] + tod[2]
    
    for i in range(len(privacies)):
        s = privacies[i].split(" ")
        day = s[0].split(".")
        pmm = int(day[1]) +int(dic[s[1]])
        pyy = int(day[0])
        pdd = int(day[2])
        while pmm > 12:
            pyy += 1
            pmm -= 12
        if pdd == 1:
            pdd = 28
            pmm -= 1
        else:
            pdd -= 1
            
        pyy = str(pyy)
        if pmm < 10:
            pmm = "0" + str(pmm)
        else:
            pmm = str(pmm)
        if pdd < 10:
            pdd = "0" + str(pdd)
        else:
            pdd = str(pdd)
        ppp = int(pyy+ pmm + pdd)

        if int(ttt) > ppp:
            result.append(i+1)
    return result
