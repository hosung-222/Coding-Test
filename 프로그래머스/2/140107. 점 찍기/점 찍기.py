import math
def solution(k, d):
    answer = 0
    max = d * d
    for a in range(d+1):
        x = (max - ((a*k)**2))
        if x >= 0:

            answer += math.sqrt(x)//k +1
    return answer