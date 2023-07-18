from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer =[]
    for i in course:
        temp = []
        for order in orders:
            temp += combinations(sorted(order),i)
        counter = Counter(temp)
        
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(j) for j in counter if counter[j] ==max(counter.values())]
            
    return sorted(answer)
            

    