# def solution(prices):
#     answer = [0]*len(prices)
#     for i in range(len(prices)):
#         cnt = 0
#         for j in range(i+1,len(prices)):
#             if prices[i] <= prices[j]:
#                 cnt += 1
#             else:
#                 cnt += 1
#                 break
#         answer[i] = cnt
#     return answer

def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
            stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer

        
    