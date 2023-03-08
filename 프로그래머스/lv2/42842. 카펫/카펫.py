def solution(brown, yellow):
    x = brown-4
    xx = x//2
    for i in range(1,xx//2+1):
        if i * (xx-i) == yellow:
            return [xx-i+2,i+2]