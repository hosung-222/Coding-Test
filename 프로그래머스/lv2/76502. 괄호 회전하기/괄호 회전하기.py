from collections import deque
def solution(s):
    dic = { '[':']', '{':'}', '(':')'}
    dq = deque(s)
    cnt = 0
    for k in range(len(s)):
        stack = []
        for i in range(len(s)):
            if dq[i] in ('[','{','('):
                stack.append(dq[i])
            else:
                if len(stack) == 0:
                    stack.append('x')
                    break
                elif dq[i] == dic[stack[-1]]:
                    stack.pop()
                else:
                    stack.append('x')
                    break
                    
        dq.append(dq.popleft())
        if len(stack) == 0:
            cnt += 1

    return cnt
        