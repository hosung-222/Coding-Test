from collections import defaultdict 
import sys

n, m = map(int, input().split())
words_count = defaultdict(int)
for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) >= m:
        words_count[word] += 1

words = sorted(words_count.keys(), key=lambda x: (-words_count[x], -len(x), x))
for word in words:
    print(word)