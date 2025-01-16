word = input()
i = len(word)

frame = [['.' for _ in range(5 + 4 * (i - 1))] for j in range(5)]
for idx in range(i):
    frame[0][2 + 4 * idx] = '#' if (idx + 1) % 3 != 0 else '*'
    frame[2][2 + 4 * idx] = word[idx]
    frame[4][2 + 4 * idx] = '#' if (idx + 1) % 3 != 0 else '*'

for idx in range(1, len(frame[0]), 2):
    frame[1][idx] = '#'
    frame[3][idx] = '#'

idx = 0
for j in range(2, len(frame[0]) - 2):
    if frame[2][j] == word[idx]:
        if (idx + 1) % 3 == 0:
            frame[1][j - 1] = '*'
            frame[1][j + 1] = '*'
            frame[2][j - 2] = '*'
            frame[2][j + 2] = '*'
            frame[3][j - 1] = '*'
            frame[3][j + 1] = '*'
        else:
            if frame[2][j - 2] == '.':
                frame[2][j - 2] = '#'
            frame[2][j + 2] = '#'
        idx += 1

for i in range(5):
    print(''.join(frame[i]))