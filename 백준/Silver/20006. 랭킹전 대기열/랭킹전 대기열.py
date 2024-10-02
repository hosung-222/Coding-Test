player, maximum = map(int, input().split())

rooms = []
room_nickname = []
for i in range(player):
    level, nickname = input().split()
    if len(rooms) == 0:
        rooms.append(int(level))
        room_nickname.append([(level, nickname)])
    else:
        in_room = False
        for i in range(len(rooms)):
            if rooms[i]+10 >= int(level) >= rooms[i]-10 and len(room_nickname[i]) < maximum:
                room_nickname[i].append((int(level), nickname))
                in_room = True
                break
        if not in_room:
            rooms.append(int(level))
            room_nickname.append([(level, nickname)])

for i in range(len(room_nickname)):
    room_nickname[i].sort(key=lambda x: x[1])

    if len(room_nickname[i]) == maximum:
        print("Started!")
    else:
        print("Waiting!")
    for level, nickname in room_nickname[i]:
        print(level, nickname)
