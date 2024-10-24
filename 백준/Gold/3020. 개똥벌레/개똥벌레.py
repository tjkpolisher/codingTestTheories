import sys
input = sys.stdin.readline

N, H = map(int, input().split())
hazards = {i: 0 for i in range(H)}
for i in range(1, N + 1):
    if i % 2 == 1:  # 첫번째 및 홀수 번째 장애물은 석순
        hazards[0] += 1
        hazards[int(input())] -= 1
    else:
        hazards[H - int(input())] += 1

array = list(hazards.values())
prefix = [array[0]]
for i in range(H - 1):
    prefix.append(prefix[i] + array[i + 1])

minimum_collision = min(prefix)  # 최소 충돌 횟수
num_lane = 0  # 최소 충돌 구간의 개수
for i in range(H):
    if prefix[i] == minimum_collision:
        num_lane += 1

print(minimum_collision, num_lane)