N = int(input())
words = []

for _ in range(N):
    word = input()
    words.append(word)

for word in words:
    if word[::-1] in words:
        print(len(word), word[len(word) // 2])
        break
    elif word[::-1] == word:
        print(len(word), word[len(word) // 2])
        break