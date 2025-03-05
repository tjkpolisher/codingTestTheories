import sys
input = sys.stdin.readline

N, D = map(int, input().split())
gift = []
for _ in range(N):
    P, V = map(int, input().split())
    gift.append((P, V))

gift.sort(key=lambda x: x[0])

ans = 0  # 정답(실제 만족도)
tmp = 0  # 만족도를 저장하는 임시 변수
i = 0  # 포인터 1
j = 0  # 포인터 2

while j < N:
    if gift[j][0] - gift[i][0] < D:
        tmp += gift[j][1]
        j += 1
    else:
        ans = max(ans, tmp)
        p = gift[j][0] - D + 1
        while p > gift[i][0]:
            tmp -= gift[i][1]
            i += 1

ans = max(ans, tmp)
print(ans)