from collections import Counter

word1 = Counter(input())
word2 = Counter(input())

counter = (word1 - word2) + (word2 - word1)

print(sum(counter.values()))