from collections import deque
import sys

result = list(sys.stdin.readline().rstrip())
left_list = deque(result)
right_list = deque()

m = int(sys.stdin.readline())
for _ in range(m):
    command = list(sys.stdin.readline().split())
    
    if command[0] == 'L':
        if len(left_list):
            right_list.appendleft(left_list.pop())
    
    elif command[0] == 'D':
        if len(right_list):
            left_list.append(right_list.popleft())
    
    elif command[0] == 'B':
        if len(left_list):
            left_list.pop()

    elif command[0] == 'P':
        left_list.append(command[1])

print(''.join(left_list) + ''.join(right_list))
