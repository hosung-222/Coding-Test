n = list(input())
balls = list(input().strip())

red_balls = balls.copy()
blue_balls = balls.copy()

result = int(1e9)
find = False
count = 0
for i in range(len(red_balls)-1, -1, -1):
    if red_balls[i] == "B":
        find = True
    
    if red_balls[i] == "R" and find == True:
        count += 1
    
result = min(result, count)
count = 0
find = False
for i in range(len(red_balls)):
    if red_balls[i] == "B":
        find = True
    
    if red_balls[i] == "R" and find == True:
        count += 1
result = min(result, count)
count = 0
find = False
for i in range(len(blue_balls)-1, -1, -1):
    if blue_balls[i] == "R":
        find = True
    
    if blue_balls[i] == "B" and find == True:
        count += 1
result = min(result, count)
count = 0
b_find = False
for i in range(len(blue_balls)):
    if blue_balls[i] == "R":
        find = True
    
    if blue_balls[i] == "B" and find == True:
        count += 1
result = min(result, count)
print(min(result, count))