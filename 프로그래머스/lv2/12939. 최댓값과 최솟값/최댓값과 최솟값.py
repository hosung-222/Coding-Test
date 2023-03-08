def solution(s):
    s.split()
    nums = []
    for i in s.split():
        nums.append(int(i))
    return str(min(nums)) + " " + str(max(nums))
    
    
    
        