N, L = map(int, input().split())


def partial_sum(n, a):
    return n * (2 * a + n - 1) // 2


for size in range(L, 101):
    ans_list = []
    start = max(N // size - size // 2, 0)
    for a in range(start, start + size + 1):
        if partial_sum(size, a) == N:
            ans_list = list(range(a, a + size))
            break
    if ans_list:
        print(*ans_list)
        break
else:
    print(-1)