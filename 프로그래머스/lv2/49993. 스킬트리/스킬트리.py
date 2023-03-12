def solution(skill, skill_trees):
    cnt = 0
    for i in skill_trees:
        x = skill
        s = True
        for j in i:
            if j in x and j == x[0]:
                x = x[1:]
            elif j not in x:
                continue
            else:
                s= False
                break
        if s :
            cnt += 1
    return cnt
            