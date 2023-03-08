def solution(msg):
    dic = [chr(i+64) for i in range(1,27)]
    now = msg[0]
    answer = []
    i = 0
    while i < len(msg):
        if now in dic:
            if i == (len(msg)-1):
                answer.append(dic.index(now)+1)
                break
            else:
                i += 1
            now += msg[i]
        else:
            dic.append(now)
            answer.append(dic.index(now[:-1])+1)
            now = msg[i]
    return answer