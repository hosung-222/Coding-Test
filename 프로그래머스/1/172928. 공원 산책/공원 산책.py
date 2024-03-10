def solution(park, routes):
    dict = {"N": (-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    x, y = 0, 0
    max_w, max_h = len(park[0]), len(park)
    for i in range(len(park)):
        if 'S' in park[i]:
            y = i
            x = park[i].index('S')
            break

    for r in routes:
        direction, count = r[0], int(r[2])
        tx, ty = x, y
        
        for i in range(count):
            nx = x + dict[direction][1]
            ny = y + dict[direction][0]
            
            if 0<=nx<max_w and 0<=ny<max_h and park[ny][nx] != "X":
                
                x, y = nx, ny
            else:
                x, y = tx, ty
                break
                

    return (y,x)