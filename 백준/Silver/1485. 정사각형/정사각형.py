T = int(input())


def length(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


for _ in range(T):
    coords = []
    for i in range(4):
        x, y = map(int, input().split())
        coords.append((x, y))
    coords.sort(key=lambda x: (x[0], x[1]))
    coords[2], coords[3] = coords[3], coords[2]

    # 대각선 길이 체크
    diag1 = length(coords[0], coords[2])
    diag2 = length(coords[1], coords[3])
    if diag1 != diag2:
        print(0)
        continue

    # 길이 체크
    lengths = set()
    for i in range(4):
        if i == 3:
            lengths.add(length(coords[3], coords[0]))
        else:
            lengths.add(length(coords[i], coords[i + 1]))
    if len(lengths) > 1:
        print(0)
    else:
        print(1)