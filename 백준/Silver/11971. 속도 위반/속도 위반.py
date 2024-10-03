N, M = map(int, input().split())
road = {}
rider = {}

interval_orig = 1
for _ in range(N):
    interval, speed = map(int, input().split())
    for i in range(interval_orig, interval_orig + interval):
        road[i] = speed
    interval_orig += interval
interval_orig = 1
for _ in range(M):
    interval, speed = map(int, input().split())
    for i in range(interval_orig, interval_orig + interval):
        rider[i] = speed
    interval_orig += interval

over = 0  # 속도 위반한 최대값
for d in range(1, 101):
    # 1km ~ 100km까지 속도 측정
    diff = max(rider[d] - road[d], 0)
    over = max(diff, over)

print(over)