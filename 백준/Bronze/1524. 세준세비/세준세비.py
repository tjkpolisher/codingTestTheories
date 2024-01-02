T = int(input())
for _ in range(T):
    blank = input()
    N, M = map(int, input().split())
    sj = list(map(int, input().split()))
    sb = list(map(int, input().split()))
    maximum_power = max(max(sj), max(sb))
    if maximum_power in sj and maximum_power in sb:
        print("S")
    elif maximum_power in sb:
        print("B")
    else:
        print("S")