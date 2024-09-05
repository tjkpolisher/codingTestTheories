import sys
input = sys.stdin.readline

N, M = map(int, input().split())
prices = []
for _ in range(M):
    prices.append(int(input()))

prices.sort(reverse=True)
revenue = 0
for i in range(M):
    tmp_price = prices[i]
    if i + 1 <= N:
        tmp_revenue = tmp_price * (i + 1)
        if tmp_revenue > revenue:
            revenue = tmp_revenue
            A = tmp_price
    else:
        break
print(A, revenue)