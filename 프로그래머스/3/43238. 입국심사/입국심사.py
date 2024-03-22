def solution(n, times):
    answer = 0
    left, right = 0, max(times)*n
    
    while left <= right:
        p = 0
        mid = (left + right) //2
        for i in times:
            p += mid // i
            if p >= n:
                break
        if p >= n:
            answer = mid
            right = mid -1
        else:
            left = mid + 1
    
    return answer