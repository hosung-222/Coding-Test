import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    c = input().split()
    
    if c[0] == 'push':
        a.append(c[1])
    elif c[0] == 'pop':
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop(0))
    elif c[0] == 'size':
        print(len(a))
    elif c[0] == 'empty':
        if len(a) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(a) == 0:
            print(-1)
        else:
            print(a[0])
    elif c[0] == 'back':
        if len(a) == 0:
            print(-1)
        else:
            print(a[-1])
