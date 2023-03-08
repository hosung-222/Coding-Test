def solution(elements):
    a = set()
    eLen = len(elements)
    elements *= 2
    
    for i in range(eLen):
        for j in range(eLen):
            a.add(sum(elements[j:j+i+1]))
    return len(a)