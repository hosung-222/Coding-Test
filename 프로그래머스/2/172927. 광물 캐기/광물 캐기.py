def solution(picks, minerals):
    answer = 0
    dia, iron, stone = picks[0], picks[1], picks[2]
    allmine = dia + iron + stone
    if len(minerals) > allmine * 5:
        minerals = minerals[:allmine * 5]
    
    minerals_5 = [[0,0,0] for _ in range(len(minerals)//5 + 1)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            minerals_5[i//5][0] += 1
        elif minerals[i] == 'iron':
            minerals_5[i//5][1] += 1
        elif minerals[i] == 'stone':
            minerals_5[i//5][2] += 1
    
    minerals_5.sort(key=lambda x:(-x[0], -x[1], -x[2]))
    
    for m in minerals_5:
        d, i, s = m
        for p in range(3):
            if picks[p]>0 and p==0:
                picks[p] -= 1
                answer += d+i+s
                break
            elif picks[p]>0 and p==1:
                picks[p] -= 1
                answer += (d*5)+i+s
                break
            elif picks[p]>0 and p==2:
                picks[p] -= 1
                answer += (d*25)+(i*5)+s
                break
    
    return answer