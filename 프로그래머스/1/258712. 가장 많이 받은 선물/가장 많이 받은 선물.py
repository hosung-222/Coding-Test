def solution(friends, gifts):
    
    gift_trace = {f1: {f2: 0 for f2 in friends if f1 != f2} for f1 in friends}
    give_count = {f: 0 for f in friends}
    receive_count = {f: 0 for f in friends}
    answer = {f: 0 for f in friends}
    
    
    for gift in gifts:
        giver, receiver = gift.split()
        gift_trace[giver][receiver] += 1
        give_count[giver] += 1
        receive_count[receiver] += 1
        
    for i in range(len(friends) -1):
        for j in range(i+1, len(friends)):
            a = friends[i]
            b = friends[j]
            a_count = gift_trace[a][b]
            b_count = gift_trace[b][a]
            
            if a_count > b_count:
                answer[a] += 1
            elif a_count < b_count:
                answer[b] += 1
            else:
                a_value = give_count[a] - receive_count[a]
                b_value = give_count[b] - receive_count[b]
                if a_value > b_value:
                    answer[a] += 1
                elif a_value < b_value:
                    answer[b] += 1
                    

    return max(answer.values())