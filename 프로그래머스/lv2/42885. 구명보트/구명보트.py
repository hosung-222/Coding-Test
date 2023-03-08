def solution(people, limit):
    people.sort()
    cnt = 0
    left = 0
    right = len(people)-1
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        cnt += 1
    return cnt
        
                