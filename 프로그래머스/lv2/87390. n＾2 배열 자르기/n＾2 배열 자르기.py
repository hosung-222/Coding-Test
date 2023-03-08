def solution(n, left, right):
    answer = []
    cnt = left
    while left<= cnt <= right:
        answer.append(max(cnt//n+1, cnt%n+1))
        cnt+= 1
    return answer