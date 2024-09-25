directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

n, m, x, y, k = map(int, input().split())  # n: 세로, m: 가로, x: 주사위 시작 x 좌표, y: 주사위 시작 y 좌표, k: 명령 개수
matrix = [list(map(int, input().split())) for _ in range(n)]  # n x m 크기의 지도 정보를 입력받음
command = list(map(int, input().split())) # 동 1 서 2 북 3 남 4

dice = [0, 0, 0, 0, 0, 0] #위(0), 아래(1), 앞(2), 뒤(3), 왼(4), 오(5)
def roll_dice(direction):
    top, bottom, front, back, left, right = dice
    if direction == 1: #동쪽
        dice[0], dice[1], dice[4], dice[5] = left, right, bottom, top
    elif direction == 2: #서쪽
        dice[0], dice[1], dice[4], dice[5] = right, left, top, bottom
    elif direction == 3: # 북쪽
        dice[0], dice[1], dice[2], dice[3] = front, back, bottom, top
    elif direction == 4: # 남쪽
        dice[0], dice[1], dice[2], dice[3] = back, front, top, bottom



for c in command:
    index = (c-1)
    dx, dy = directions[index]
    nx, ny = x + dx, y + dy

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    
    roll_dice(c)
    # 이동 칸이 0인경우 : 주사위 바닥면의 숫자 -> 칸의 수
    if matrix[nx][ny] == 0 :
        matrix[nx][ny] = dice[1]

    # 이동 칸이 0이 아닌 경우 : 칸의 숫자 -> 주사위 바닥
    else:
        dice[1] = matrix[nx][ny]
        matrix[nx][ny] = 0
    
    print(dice[0])
    x, y = nx, ny
