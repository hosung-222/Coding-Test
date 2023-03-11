def solution(prices):
    answer = [0]*len(prices)
    index= 0
    x= 0
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                if answer[i] == 0:
                    cnt += 1
                break
        answer[i] = cnt
    return answer
            
                    
            
        
    