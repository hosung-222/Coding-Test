n = list(input())
balls = list(input().strip())

red_balls = balls.copy()
blue_balls = balls.copy()

blue_count = 0
red_count = 0
b_find = False
r_find = False
for i in range(len(red_balls)-1, -1, -1):
    if red_balls[i] == "B":
        b_find = True
    
    if red_balls[i] == "R" and b_find == True:
        red_count += 1

for i in range(len(blue_balls)-1, -1, -1):
    if blue_balls[i] == "R":
        r_find = True
    
    if blue_balls[i] == "B" and r_find == True:
        blue_count += 1

print(min(blue_count, red_count))