def solution(wallpaper):
    sx, sy, ex, ey = 50,50,0,0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                if i < sx :
                    sx = i
                if j < sy:
                    sy = j
                if i > ex :
                    ex = i
                if j > ey:
                    ey = j
    return [sx,sy,ex+1,ey+1]