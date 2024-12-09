import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    N_bin = bin(N)[2:]
    ans = int(N_bin, 3)
    print(ans)