import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x = int(input())
    if x == 0:
        print(0)
        continue

    if x > 0:
        k = x.bit_length() - 1
        p = 2 ** k
        if p < x:
            k += 1
        print(2 ** (k + 2) + x - 4)
    else:
        nx = -x
        k = nx.bit_length() - 1
        p = 2 ** k
        if p < nx:
            k += 1
        print(6 * 2 ** k - x - 4)