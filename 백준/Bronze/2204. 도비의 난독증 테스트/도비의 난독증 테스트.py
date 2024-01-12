while True:
    n = int(input())
    if n == 0:
        break
    words = []
    words_lower = []
    for i in range(n):
        s = input()
        words.append(s)
        words_lower.append(s.lower())
    words_sorted = sorted(words_lower)
    idx = [words_lower.index(word) for word in words_sorted]
    words = [words[i] for i in idx]
    print(words[0])