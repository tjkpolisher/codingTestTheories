from collections import defaultdict

N = int(input())
words = []
for _ in range(N):
    word = input()
    word_dict = defaultdict(int)
    for c in word:
        word_dict[c] += 1
    if word_dict not in words:
        words.append(word_dict)

print(len(words))