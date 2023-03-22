from itertools import *
def solution(numbers):
    arr = list(numbers)
    result = []
    for i in range(1,len(arr)+1):
        nPr = permutations(arr, i)
        result += nPr
    answer = []
    for i in result:
        answer.append(int(''.join(i)))
    answer = set(answer)
    cnt = 0
    
    #소수인지 확인
    for i in answer:
        b = 0
        if i!= 1 and i!=0:
            for j in range(2,int(i**0.5)+1):
                if i % j == 0:
                    b = 1
            if b == 0:
                cnt += 1
    return cnt