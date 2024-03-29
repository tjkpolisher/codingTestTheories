def next_number(n):
    return n // 2 + 1 if n % 2 == 1 else n // 2


N, n1, n2 = map(int, input().split())
if n1 > n2:
    n1, n2 = n2, n1
cnt = 1  # 몇 라운드에서 만나는지를 나타내는 카운터(1라운드부터 시작)
while True:
    if n2 - n1 == 1 and n2 % 2 == 0:
        break
    cnt += 1
    N //= 2
    n1, n2 = next_number(n1), next_number(n2)

print(cnt)