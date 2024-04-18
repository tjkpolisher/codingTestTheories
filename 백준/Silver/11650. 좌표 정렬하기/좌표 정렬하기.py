import sys
input = sys.stdin.readline

N = int(input())
coordinates = []
for _ in range(N):
    coordinates.append(list(map(int, input().split())))

coordinates.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(coordinates[i][0], coordinates[i][1])