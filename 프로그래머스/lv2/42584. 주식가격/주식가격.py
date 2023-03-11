# def solution(prices):
#     answer = [0]*len(prices)
#     index= 0
#     x= 0
#     for i in range(len(prices)):
#         cnt = 0
#         for j in range(i+1,len(prices)):
#             if prices[i] <= prices[j]:
#                 cnt += 1
#                 print (i, cnt, answer)
#             else:
#                 print (i, cnt,answer)
#                 if answer[i] == 0:
#                     cnt += 1
#                 break
#         answer[i] = cnt
#     return answer

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer            
                    
            
        
    