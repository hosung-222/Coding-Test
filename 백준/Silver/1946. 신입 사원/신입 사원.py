import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    result = 1
    n = int(input())
    score = []
    for _ in range(n):
        score.append(list(map(int, input().split())))
    
    score.sort(key=lambda x: x[0])
    min_interview_score = score[0][1]

    for i in range(1,n):
        if score[i][1] < min_interview_score:
            result += 1
            min_interview_score = score[i][1]

    print(result)