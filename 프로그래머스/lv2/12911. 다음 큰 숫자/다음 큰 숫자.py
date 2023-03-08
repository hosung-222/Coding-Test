def solution(n):
    b_n = format(n,'b')
    while True:
        n += 1
        x = format(n,'b')
        if x.count('1') == b_n.count('1'):
            return n