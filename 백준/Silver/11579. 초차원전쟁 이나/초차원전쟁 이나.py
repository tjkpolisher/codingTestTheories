import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    moves = [list(map(int, input().split())) for _ in range(n)]
    coords = list(map(int, input().split()))

    ans = 0
    ok = True

    for r in range(n):
        c = coords[r]
        if c < 0:
            print(0)
            ok = False
            break

        u_r = c
        ans += u_r
        if ans > 2 * 10 ** 9:
            print(0)
            ok = False
            break

        for j in range(r, n):
            coords[j] -= u_r * moves[r][j]

    if ok:
        print(1, ans)