N = int(input())
cnt = N

for _ in range(N):
    word = input()
    unique = set()
    for i, c in enumerate(word):
        if i == 0:
            unique.add(c)
        elif c != word[i-1] and c not in unique:
            unique.add(c)
        elif c != word[i-1] and c in unique:
            cnt -= 1
            break

print(cnt)