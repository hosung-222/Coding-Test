from collections import deque
def solution(A, B):
    answer = 0
    A.sort(reverse =True)
    B.sort(reverse =True)
    a = deque(A)
    b = deque(B)
    for i in range(len(A)):
        if a[0] >= b[0]:
            a.popleft()
            b.pop()
        elif b[0] > a[0]:
            a.popleft()
            b.popleft()
            answer += 1
    return answer