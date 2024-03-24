N, M = map(int, input().split())
price_package = []  # 패키지 가격
price_single = []  # 낱개 가격
for _ in range(M):
    p, s = map(int, input().split())
    price_package.append(p)
    price_single.append(s)

price_package.sort()
price_single.sort()
package, single = divmod(N, 6)  # N을 6으로 나눴을 때의 몫과 나머지

p1 = package * price_package[0] + single * price_single[0]
p2 = (package + 1) * price_package[0]
p3 = N * price_single[0]

print(min(min(p1, p2), p3))