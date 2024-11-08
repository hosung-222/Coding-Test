s = list(input())

len_one = s.count("1")//2
len_zero = s.count("0")//2

for _ in range(len_one):
    s.pop(s.index("1"))

s = s[::-1]
for _ in range(len_zero):
    s.pop(s.index("0"))

    
print("".join(s[::-1]))