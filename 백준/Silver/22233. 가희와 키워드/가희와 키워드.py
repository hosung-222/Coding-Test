import sys
input = sys.stdin.readline
n, m = map(int, input().split())
keywords = set()
for _ in range(n):
    keywords.add(input().strip())

for _ in range(m):
    posts = list(input().strip().split(","))
    for post in posts:
        keywords.discard(post)
    print(len(keywords))
