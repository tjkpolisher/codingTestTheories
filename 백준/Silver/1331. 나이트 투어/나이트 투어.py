visited = [[False] * 6 for _ in range(6)]  # 좌표 방문 여부 체크
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(36):
    coord = input()
    x = alphabets.index(coord[0])
    y = int(coord[1]) - 1

    if i == 0:
        orig_x = alphabets.index(coord[0])
        orig_y = int(coord[1]) - 1
        ox = orig_x
        oy = orig_y
        visited[y][x] = True
        continue

    for j in range(8):
        nx = ox + dx[j]
        ny = oy + dy[j]
        if 0 <= nx < 6 and 0 <= ny < 6 and nx == x and ny == y:
            visited[ny][nx] = True
            ox = nx
            oy = ny
            break


def is_valid():
    for i in range(6):
        for j in range(6):
            if not visited[j][i]:
                return "Invalid"
    return "Valid"


# 마지막 체크
for i in range(8):
    nx = ox + dx[i]
    ny = oy + dy[i]
    if 0 <= nx < 6 and 0 <= ny < 6 and nx == orig_x and ny == orig_y:
        print(is_valid())
        break
else:
    print("Invalid")