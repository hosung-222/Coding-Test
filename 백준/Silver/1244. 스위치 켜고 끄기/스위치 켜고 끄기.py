n = int(input())
switch = list(map(int, input().split()))
student = int(input())

def switch_number(index):
    if switch[index] == 0:
        switch[index] = 1
    else:
        switch[index] = 0

for _ in range(student):
    sex, number = map(int, input().split())
    if sex == 1: # 남자
        for i in range(number-1, n, number):
            switch_number(i)
    
    else: # 여자
        switch_number(number-1)
        for i in range(1, len(switch)//2):
            if number-i-1 < 0 or number+i-1 >= len(switch):
                break
            if switch[number-i-1] == switch[number+i-1]:
                switch_number(number-i-1)
                switch_number(number+i-1)
            else:
                break

for i in range(0, len(switch), 20):
    print(*switch[i:i+20])