li, m = [], []

while True:
    try:
        line = input().rstrip().split()
        li.append(line)
        for i, l in enumerate(line):
            if i < len(m):
                m[i] = max(m[i], len(l))
            else:
                m.append(len(l))
    except EOFError:
        break

for i, l in enumerate(li):
    for j, w in enumerate(l):
        li[i][j] = w + (m[j] - len(w)) * ' '

for l in li:
    print(' '.join(l).rstrip())