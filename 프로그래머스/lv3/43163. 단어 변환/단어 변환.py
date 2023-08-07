from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque()
    q.append([begin, 0])

    while q:
        s, idx = q.popleft()
        if s == target:
            return idx
        cnt = 0
        for i in range(len(words)):
            cnt = 0
            word = words[i]
            for j in range(len(s)):
                if s[j] != word[j]:
                    cnt += 1
            if cnt == 1:
                q.append([word, idx + 1])
                
    return 0