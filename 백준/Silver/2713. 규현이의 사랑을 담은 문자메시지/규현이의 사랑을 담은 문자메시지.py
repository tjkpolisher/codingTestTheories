import sys
input = sys.stdin.readline

T = int(input())
char_num_dict = {' ': 0}
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    char_num_dict[char] = ord(char) - ord('A') + 1

for _ in range(T):
    parts = input().rstrip().split(' ', 2)
    R, C = int(parts[0]), int(parts[1])
    message = parts[2] if len(parts) > 2 else ""

    R, C = int(R), int(C)

    matrix = [[None for i in range(C)] for j in range(R)]
    movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    direction = 0

    for char in message:
        char_num = char_num_dict[char]  # 문자를 숫자로 변환
        char_bin = bin(char_num)[2:].zfill(5)  # 숫자를 다섯 자리 이진수로 변환

        for bit in char_bin:
            matrix[x][y] = bit
            dx, dy = movement[direction]
            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C and matrix[nx][ny] is None:
                x, y = nx, ny
            else:
                direction = (direction + 1) % 4
                dx, dy = movement[direction]
                x, y = x + dx, y + dy

    output = []
    for row in matrix:
        for cell in row:
            output.append(cell if cell is not None else '0')
    print(''.join(output))