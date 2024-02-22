# 출처: 2019 국가 교육기관 코딩 테스트
N, M = map(int, input().split())
ans = 0
for _ in range(N):
    minimum = min(list(map(int, input().split())))
    ans = max(ans, minimum)
print(ans)
