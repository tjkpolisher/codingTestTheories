# 출처: 2018 E 기업 알고리즘 대회
N, K = map(int, input().split())
cnt = 0

while N > 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    cnt += 1

print(cnt)
