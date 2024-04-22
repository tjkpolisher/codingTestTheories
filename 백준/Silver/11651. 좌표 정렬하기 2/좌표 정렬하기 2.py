import sys
input = sys.stdin.readline

N = int(input())
coordinates = []
for _ in range(N):
    x_i, y_i = map(int, input().split())
    coordinates.append((x_i, y_i))

coordinates.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
    print(coordinates[i][0], coordinates[i][1])