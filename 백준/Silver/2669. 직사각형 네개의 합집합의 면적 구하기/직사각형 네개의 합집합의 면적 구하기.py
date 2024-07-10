import sys
input = sys.stdin.readline

square_array = [[0] * 101 for _ in range(101)]
area = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    # 이중 반복문 수행
    for i in range(x1, x2):
        for j in range(y1, y2):
            if not square_array[i][j]:
                square_array[i][j] = 1
                area += 1

print(area)