T = int(input())
for _ in range(T):
    ans = 0
    a, b, c = map(int, input().split())
    for x in range(1, a + 1):
        for y in range(x, b + 1):
            for z in range(y, c + 1):
                if x % y == y % z and y % z == z % x:
                    ans += 1
    print(ans)