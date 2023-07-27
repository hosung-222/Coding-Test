def solution(tickets):
    answer = []
    dic = {}
    q = ["ICN"]
    for s, e in tickets:
        if s not in dic:
            dic[s] = [e]
        else:
            dic[s].append(e)
    
    for k in dic.keys():
        dic[k].sort(reverse=True)
    
    while q:
        top = q[-1]
        #더 이상 갈 수 있는 도착지가 없을때
        if (top not in dic) or (not dic[top]):
            answer.append(q.pop())

        else:
            q.append(dic[top].pop())

    return answer[::-1]