T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    A.sort()
    print(A[-3])