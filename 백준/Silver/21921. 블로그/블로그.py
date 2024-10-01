n, m = map(int, input().split())
view = list(map(int, input().split()))

max_day = 1
max_view = sum(view[:m])
temp_view = max_view

for i in range(m, n):
    temp_view = temp_view - view[i - m] + view[i]
    if temp_view > max_view:
        max_day = 1
        max_view = temp_view
    elif temp_view == max_view:
        max_day+=1

if max_view == 0:
    print("SAD")
else:
    print(max_view)
    print(max_day)