import itertools
from collections import deque

def solution(expression):
    answer = []
    mod = ["*", "+", "-"]
    npr = list(itertools.permutations(mod, 3))
    stack = deque()
    num = ""

    for t in expression:
        if t not in mod:
            num += t
        else:
            stack.append(int(num))
            stack.append(t)
            num = ""
    stack.append(int(num))  
    
    for ops in npr:
        temp_stack = stack.copy()
        for op in ops:
            new_stack = deque()
            while temp_stack:
                token = temp_stack.popleft()
                if token == op:
                    num1 = new_stack.pop()
                    num2 = temp_stack.popleft()
                    new_stack.append(operation(num1, num2, op))
                else:
                    new_stack.append(token)
            temp_stack = new_stack.copy()
        answer.append(abs(temp_stack[-1]))
    return max(answer)

def operation(num1, num2, mod):
    if mod == "+":
        return num1 + num2
    elif mod == "-":
        return num1 - num2
    elif mod == "*":
        return num1 * num2


