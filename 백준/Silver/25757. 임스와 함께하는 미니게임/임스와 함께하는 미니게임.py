n, game_type = input().split()

palayer = set()
for i in range(int(n)):
    palayer.add(input())

if game_type == 'Y':
    print(len(palayer))
elif game_type == 'F':
    print(len(palayer) // 2)
elif game_type == 'O':
    print(len(palayer) // 3)