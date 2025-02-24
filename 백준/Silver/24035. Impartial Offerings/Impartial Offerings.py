import sys
input = sys.stdin.readline

T = int(input())
for idx in range(T):
    N = int(input())
    sizes = list(map(int, input().split()))

    sizes.sort()
    ans = 1
    treat = 1
    for i in range(1, N):
        if sizes[i] > sizes[i - 1]:
            treat += 1
        ans += treat
    print(f"Case #{idx + 1}: {ans}")