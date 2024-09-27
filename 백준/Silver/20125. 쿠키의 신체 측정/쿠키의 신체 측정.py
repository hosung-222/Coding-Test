n = int(input())
cookie = []
for i in range(n):
    cookie.append(list(input().strip())) 

head_x, head_y = 0, 0

left_arm, right_arm = 0, 0
body_length = 0
left_leg, right_leg = 0, 0

# 머리 찾기
for i in range(n):
    for j in range(len(cookie[i])):
        if cookie[i][j] == "*":
            head_x, head_y = i, j  # 머리 위치 저장
            break
    if head_x != 0 or head_y != 0:
        break  

heart_x, heart_y = head_x + 1, head_y

# 팔 찾기
for i in range(len(cookie[0])):
    if cookie[heart_x][i] == "*" and i < heart_y:
        left_arm += 1
    elif cookie[heart_x][i] == "*" and i > heart_y:
        right_arm += 1

# 몸통 찾기
for i in range(head_x+1, n):
    if cookie[i][head_y] == "*":
        body_length += 1
    else:
        break

# 다리 찾기
for i in range(head_x + body_length + 1, n):
    if cookie[i][head_y - 1] == "*":  
        left_leg += 1
    if cookie[i][head_y + 1] == "*": 
        right_leg += 1

print(heart_x+1, heart_y + 1)  
print(left_arm, right_arm, body_length-1, left_leg, right_leg)
