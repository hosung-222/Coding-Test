def solution(numbers, target):
    cnt = 0
    q = [[numbers[0], 0], [numbers[0]*-1, 0]]
    while q:
        num, index = q.pop()
        index += 1
        if index < len(numbers) :
            q.append([num+numbers[index],index])
            q.append([num-numbers[index],index])
        else:
            if num == target:
                cnt += 1
    return cnt