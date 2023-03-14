def solution(dirs):
    visit = set()  
    x, y = 0, 0
    for i in dirs:
        if i == 'U' and x < 5:
            visit.add((x, y, x + 1, y))
            visit.add((x + 1, y, x, y)) 
            x += 1
        elif i == 'D' and x > -5:
            visit.add((x, y, x - 1, y))
            visit.add((x-1, y, x, y)) 
            x -= 1
        elif i == 'L' and y > -5:
            visit.add((x, y, x, y - 1))
            visit.add((x, y-1, x, y)) 
            y -= 1
        elif i == 'R' and y < 5:
            visit.add((x, y, x, y + 1))
            visit.add((x, y+1, x , y)) 
            y += 1
    return len(visit)//2
        
        