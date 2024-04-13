import sys
K, N = map(int, input().split())
lan = []
for _ in range(K):
    lan.append(int(sys.stdin.readline().rstrip()))

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lan:
        lines += (i // mid)

    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)