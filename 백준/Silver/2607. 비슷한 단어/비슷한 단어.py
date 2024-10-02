from collections import Counter
def is_similar(word1, word2):
    if abs(len(word1) - len(word2)) > 1:
        return False
    
    count1 = Counter(word1)
    count2 = Counter(word2)
    
    diff = sum((count1 - count2).values()) + sum((count2 - count1).values())
    
    return diff <= 2

n = int(input())
words = [input().strip() for _ in range(n)]

first_word = words[0]
similar_count = 0

for word in words:
    if is_similar(first_word, word):
        similar_count += 1

print(similar_count - 1) 