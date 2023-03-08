def solution(want, number, discount):
    x = [[want[i]]*number[i] for i in range(len(want))]
    cnt = 0
    all_want = sum(x,[])
    for i in range(len(discount)-len(all_want)+1):
        disc = sorted(discount[i:i+len(all_want)]) 
        want = sorted(all_want)
        if disc == want:
            cnt+= 1
    return cnt
    
    
  