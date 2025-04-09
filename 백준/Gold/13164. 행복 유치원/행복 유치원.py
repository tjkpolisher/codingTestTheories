N, K = map(int, input().split())
heights = list(map(int, input().split()))  # 원생들의 키는 오름차순으로 정렬된 상태

if N == 1 or K >= N:
    print(0)
    exit()

diffs = []
for i in range(1, N):
    diffs.append(heights[i] - heights[i - 1])
diffs.sort(reverse=True)

ans = heights[-1] - heights[0] - sum(diffs[:K - 1])

print(ans)