from collections import deque

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    prices = deque(map(int, input().split()))

    remaining_prices = prices.copy()
    discounted_prices = []

    for price in prices:
        if price % 4 == 0:
            discounted_price = price * 3 // 4
            if discounted_price in remaining_prices:
                discounted_prices.append(discounted_price)
                remaining_prices.remove(discounted_price)
                remaining_prices.remove(price)

    discounted_prices.sort()

    print(f"Case #{i}: ", end='')
    print(*discounted_prices)