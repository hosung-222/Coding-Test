import string
def solution(n, t, m, p):
    list = ''
    answer = ''
    for i in range(30000):
        list += convert(i,n)
    for i in range(t):
        answer += list[(p-1)+i*m]
    return answer


tmp = string.digits + string.ascii_uppercase
def convert(num, base):
    q,r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q,base) + tmp[r]