def solution(s):
    s= s[:-2].replace("{","").replace(","," ").split("}")
    answer = []
    for n, i in enumerate(s):
        s[n] = i.split()
        
    s.sort(key=lambda x: len(x))
    
    for i in s:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
                
    return answer