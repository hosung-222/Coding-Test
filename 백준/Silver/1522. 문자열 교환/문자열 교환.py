s = input().strip()
n = len(s)
a_count = s.count('a')

if a_count == 0 or a_count == n:
    print(0)

else:
    extended_s = s + s[:a_count-1]
    b_count = extended_s[:a_count].count('b')
    min_swap = b_count

    for i in range(1, n):
        if extended_s[i-1] == 'b':
            b_count -= 1
        if extended_s[i + a_count -1] == 'b':
            b_count += 1
        
        min_swap = min(min_swap, b_count)
    print(min_swap)