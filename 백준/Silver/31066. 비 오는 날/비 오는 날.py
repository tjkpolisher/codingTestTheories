T = int(input())


def go_to(a, b, c, d, x, y):
    return a - x, b - y, c + x, d + y


def coming_back(a, b, c, d, z, w):
    return a + z, b + w, c - z, d - w


for _ in range(T):
    N, M, K = map(int, input().split())
    a, b, c, d = N, M, 0, 0
    cnt = 0
    if K == 1 and M == 1 and N > M:
        print(-1)
        continue

    while True:
        x = min(K * M, a)
        y = M
        a, b, c, d = go_to(a, b, c, d, x, y)
        cnt += 1
        if c == N:
            break

        z = 1
        w = M
        a, b, c, d = coming_back(a, b, c, d, z, w)
        cnt += 1

    print(cnt)