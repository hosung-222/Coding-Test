from collections import defaultdict
n = int(input())
data = []
count = defaultdict(int)
for i in range(n):
    data.append(input())

for i in data:
    for j in range(len(i)):
        count[i[-j-1]] += 1 * 10 ** (j)

count_sort = sorted(count.items(), key = lambda x: x[1], reverse=True)

alpha = {}
num = 9
for k in count_sort:
    if k[0] not in alpha:
        alpha[k[0]] = num
        num -= 1
result = 0

for i in data:
    temp = ""
    for j in i:
        temp += str(alpha[j])
    result += int(temp)
        
print(result)
  