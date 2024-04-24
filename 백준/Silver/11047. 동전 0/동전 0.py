import sys
input = sys.stdin.readline

N, K = map(int, input().split())
values = []
for _ in range(N):
    A_i = int(input())
    if A_i <= K:
        values.append(A_i)

ans = 0
while K:
    p = values.pop()
    v1, v2 = divmod(K, p)
    ans += v1
    K = v2  # 남은 가치 갱신

print(ans)