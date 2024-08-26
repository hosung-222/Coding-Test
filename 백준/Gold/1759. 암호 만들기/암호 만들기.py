from itertools import combinations
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
alphabets = list(map(str, input().split()))
ncr = list(combinations(alphabets, l))
result = []
for n in ncr:
    vowels = sum(1 for i in n if i in ['a', 'e', 'i', 'o', 'u'])
    consonants = l - vowels  # 자음의 개수는 전체 길이에서 모음의 개수를 뺀 것
    if vowels >= 1 and consonants >= 2:
        result.append(sorted(n))

result.sort()
for r in result:
    print(''.join(r))
