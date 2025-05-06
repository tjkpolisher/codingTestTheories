import sys
input = sys.stdin.readline

T, M, N = map(int, input().split())
type_map = {}
offsets = []

for _ in range(T):
    train_id, *time = input().split()
    time.pop()  # 입력받은 값의 맨 마지막의 -1을 제거
    for t in time:
        type_map[int(t)] = train_id
        offsets.append(int(t))

offsets.sort()
K = len(offsets)

start_idx = 0
for i, t in enumerate(offsets):
    if t >= M:
        start_idx = i
        break
else:
    start_idx = 0

final_idx = (start_idx + (N - 1)) % K
print(type_map[offsets[final_idx]])