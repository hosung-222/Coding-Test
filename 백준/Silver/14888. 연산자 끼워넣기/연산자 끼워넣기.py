from collections import deque
n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_value = float('-inf')
min_value = float('inf')

def dfs(i, temp):
    global max_value, min_value

    if i == n:
        max_value = max(max_value, temp)
        min_value = min(min_value, temp)
    else:
        if operators[0] > 0:
            operators[0] -= 1
            dfs(i+1, temp + numbers[i])
            operators[0] += 1

        if operators[1] > 0:
            operators[1] -= 1
            dfs(i+1, temp - numbers[i])
            operators[1] += 1

        if operators[2] > 0:
            operators[2] -= 1
            dfs(i+1, temp * numbers[i])
            operators[2] += 1
        
        if operators[3] > 0:
            operators[3] -= 1
            dfs(i+1, temp // numbers[i] if temp >= 0 else -(-temp // numbers[i]))
            operators[3] += 1

dfs(1, numbers[0])
print(max_value)
print(min_value)