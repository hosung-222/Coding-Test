def solution(order):
    sub_c = []
    main_c = [i for i in range(1,len(order)+1)]
    main_c.sort(reverse = True)
    cnt = 0
    i = 0
    while main_c:
        sub_c.append(main_c.pop())
        while sub_c:
            if sub_c[-1] == order[i]:
                sub_c.pop()
                cnt += 1
                i += 1
            else:
                break
    return cnt