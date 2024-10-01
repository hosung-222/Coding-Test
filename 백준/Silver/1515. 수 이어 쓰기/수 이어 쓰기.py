from collections import deque
num = list(map(int, input().strip()))

number = 1
now_number = list(str(number).strip())
q = deque(num)
while q:
    n = q.popleft()
    n_find = False
    while n_find == False:
        if str(n) in now_number:
            index = now_number.index(str(n))
            now_number = now_number[index+1:]
            n_find = True
            break
        else:
            number+=1
            now_number = list(str(number).strip())

print(number)
