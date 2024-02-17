N = int(input())
length_word = {}

for _ in range(N):
    word = input()
    if len(word) not in length_word:
        length_word[len(word)] = {word}
    else:
        length_word[len(word)].add(word)

for k in sorted(length_word.keys()):
    words = list(length_word[k])
    words.sort()
    for w in words:
        print(w, end='\n')