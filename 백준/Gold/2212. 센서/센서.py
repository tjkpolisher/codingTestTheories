import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
# K가 센서의 개수보다 크거나 같으면 0 출력 후 종료
if K >= N:
    print(0)
    exit()

sensors.sort()

distances = []
for i in range(1, N):
    distances.append(sensors[i] - sensors[i - 1])
distances.sort(reverse=True)

print(sum(distances[K - 1:]))