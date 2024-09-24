from collections import deque
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽(동), 아래(남), 왼쪽(서), 위(북)

def turn(direction, c):
    if c == 'L':
        return (direction - 1) % 4
    else:
        return (direction + 1) % 4

n = int(input())
k = int(input())
apples = []
for _ in range(k):
    x, y = map(int, input().split())
    apples.append((x - 1, y - 1))

l = int(input())
snake_moves = []
for _ in range(l):
    t, direction = input().split()
    snake_moves.append((int(t), direction))

snake = deque([(0, 0)])  
board = [[0] * n for _ in range(n)]  
board[0][0] = 1  
for apple in apples:
    board[apple[0]][apple[1]] = 2  # 사과가 있는 곳은 2로 표시

time = 0  # 현재 시간
direction_idx = 0  # 처음에는 오른쪽(동쪽)을 바라봄
move_idx = 0  

while True:
    time += 1
    head_x, head_y = snake[0]
    dx, dy = directions[direction_idx]
    nx, ny = head_x + dx, head_y + dy

    # 벽이나 자기 자신과 부딪혔는지 확인
    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
        break

    # 이동한 위치에 사과가 있는 경우
    if board[nx][ny] == 2:
        board[nx][ny] = 1  
        snake.appendleft((nx, ny))  # 머리를 늘림 (꼬리 안 움직임)
    else:
        board[nx][ny] = 1  
        snake.appendleft((nx, ny))  # 머리를 늘림
        tail_x, tail_y = snake.pop()  # 꼬리를 줄임
        board[tail_x][tail_y] = 0  # 꼬리가 있던 자리를 비움

    # 방향 변환이 있는 시간이 되면 방향을 바꿈
    if move_idx < l and time == snake_moves[move_idx][0]:
        direction_idx = turn(direction_idx, snake_moves[move_idx][1])
        move_idx += 1

print(time)
