n = int(input())
sequence = list(map(int, input().split()))

# 누적 합 계산
prefix = [0 for _ in range(n)]
prefix[0] = sequence[0]
for i in range(n - 1):
    prefix[i + 1] = max(prefix[i] + sequence[i + 1], sequence[i + 1])

print(max(prefix))