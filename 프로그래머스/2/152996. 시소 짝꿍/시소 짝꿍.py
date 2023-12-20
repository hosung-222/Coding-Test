from collections import defaultdict
def solution(weights):
    answer = 0
    dict = defaultdict(int)
    for i in weights:
        answer += dict[i] + dict[i*2] + dict[i/2]+ dict[(i*2)/3] + dict[(i*3)/2] + dict[(i*3)/4] +dict[(i*4)/3]
        dict[i] += 1
    return answer