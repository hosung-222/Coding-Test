def solution(record):
    dic = {}  #id : nickname
    result = []

    for i in record:
        s = i.split(" ")
        if s[0] == "Enter" or s[0] =="Change":
            dic[s[1]] = s[2]
            
    for i in record:
        s = i.split(" ")
        #s[0]: 입장/퇴장, s[1]: ID, s[2]: nickname
        if s[0] == "Enter":
            result.append(dic[s[1]]+"님이 들어왔습니다.")
        elif s[0] == "Leave":
            result.append(dic[s[1]]+"님이 나갔습니다.")
        
    return result