def solution(food):
    start = ''
    end = ''

    for i in range(1,len(food)):
        start += str(i) * (food[i]//2)
        end = str(i) * (food[i]//2) + end
    
    return start + '0' + end


# def solution(food):
#     answer = '0' 
#     for i in range(len(food)-1,0,-1): 
#         answer=str(i)*(food[i]//2)+answer
#         answer=answer+str(i)*(food[i]//2)
#     return answer