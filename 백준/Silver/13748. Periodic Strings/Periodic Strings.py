from collections import deque

s = input()
len_total = len(s)
for i in range(1, len_total // 2 + 1):
    sliced = s[:i]
    rotated = []
    deque_s = deque(sliced)
    for _ in range(i):
        rotated.append(''.join(deque_s))
        deque_s.rotate()

    for j in range(len_total // i):
        if s[i * j:i * (j + 1)] != rotated[j % i]:
            break
    else:
        print(i)
        exit()
print(len_total)