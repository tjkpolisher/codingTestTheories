import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, B = map(int, input().split())
    houses = sorted(list(map(int, input().split())))
    ans = 0
    for j in range(N):
        if ans + houses[j] > B:
            print(f"Case #{i + 1}: {j}")
            break
        ans += houses[j]
    else:
        print(f"Case #{i + 1}: {N}")