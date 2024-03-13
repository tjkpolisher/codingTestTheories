import sys
input = sys.stdin.readline

d = input().rstrip()
word = input().rstrip()

cnt = 0
if word not in d:
    pass
else:
    while len(d) >= len(word):
        if word not in d:
            break
        d = d[d.index(word) + len(word):]
        cnt += 1

print(cnt)