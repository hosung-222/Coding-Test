def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    prev1 = 1
    prev2 = 2
    for i in range(3, n+1):
        current = (prev1 + prev2) % 1000000007
        prev1 = prev2
        prev2 = current

    return current
