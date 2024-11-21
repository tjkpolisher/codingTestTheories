import sys
input = sys.stdin.readline

N, M = map(int, input().split())
coordinates = set()
for i in range(1, N + 1):  # x좌표
    for j in range(1, N + 1):  # y좌표
        coordinates.add((i, j))

for _ in range(M):
    X, Y, K = map(int, input().split())
    if len(coordinates) == 1:
        continue

    if K == 1:
        # 방향 1: x좌표가 작고, y좌표가 같은 곳
        coordinates = {(x, y) for (x, y) in coordinates if x < X and y == Y}
    elif K == 2:
        # 방향 2: x좌표가 작고, y좌표가 큰 곳
        coordinates = {(x, y) for (x, y) in coordinates if x < X and y > Y}
    elif K == 3:
        # 방향 3: x좌표가 같고, y좌표가 큰 곳
        coordinates = {(x, y) for (x, y) in coordinates if x == X and y > Y}
    elif K == 4:
        # 방향 4: x좌표가 크고, y좌표가 큰 곳
        coordinates = {(x, y) for (x, y) in coordinates if x > X and y > Y}
    elif K == 5:
        # 방향 5: x좌표가 크고, y좌표가 같은 곳
        coordinates = {(x, y) for (x, y) in coordinates if x > X and y == Y}
    elif K == 6:
        # 방향 6: x좌표가 크고, y좌표가 작은 곳
        coordinates = {(x, y) for (x, y) in coordinates if x > X and y < Y}
    elif K == 7:
        # 방향 7: x좌표가 같고, y좌표가 작은 곳
        coordinates = {(x, y) for (x, y) in coordinates if x == X and y < Y}
    elif K == 8:
        # 방향 8: x좌표가 작고, y좌표가 작은 곳
        coordinates = {(x, y) for (x, y) in coordinates if x < X and y < Y}

x, y = list(coordinates)[0]
print(x, y)