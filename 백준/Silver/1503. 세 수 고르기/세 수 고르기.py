import sys
input = sys.stdin.readline

N, M = map(int, input().split())
try:
    S = set(map(int, input().split()))
except ValueError:
    # 집합의 크기가 0인 경우 둘째 줄은 빈 줄
    S = set()

xyz_set = set(range(1, 1002)) - S

ans = 10 ** 9
for x in xyz_set:
    for y in xyz_set:
        for z in xyz_set:
            temp = x * y * z
            ans = min(ans, abs(N - temp))
            if N + 1 < temp:
                break

print(ans)