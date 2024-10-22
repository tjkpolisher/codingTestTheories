cnt = 1
while True:
    N = int(input())
    if not N:
        break
    M = 0
    i = 1
    while 5 ** i <= N:
        M += N // (5 ** i)
        i += 1

    print(f"Case #{cnt}: {M}")
    cnt += 1