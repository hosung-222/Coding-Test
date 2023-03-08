def solution(n, words):
    stack = []
    cnt = 0
    for i in words:
        cnt += 1
        if cnt >n:
            cnt = 1
        if len(stack) == 0:
            stack.append(i)
        elif i not in stack and stack[-1][-1] == i[0]:
            stack.append(i)
        else:
            return [cnt, len(stack)//n+1]
        
    return [0,0]