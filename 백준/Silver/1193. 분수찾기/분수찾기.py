X = int(input())
cnt = 0

while True:
    a1 = (cnt * (cnt + 1)) // 2
    a2 = ((cnt + 1) * (cnt + 2)) // 2
    cnt += 1
    if a1 < X <= a2:
        break

diff = a2 - X
if cnt % 2 == 0: # 짝수 번째 대각선일 때(1/N -> N / 1)
    f1 = cnt - diff
    f2 = 1 + diff
else: # 홀수 번째 대각선일 때(N/1 -> 1/N)
    f1 = 1 + diff
    f2 = cnt - diff
print(f"{f1}/{f2}")