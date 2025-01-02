N = int(input())
tides = sorted(list(map(int, input().split())))
low_tide = tides[:N // 2 + N % 2]
high_tide = tides[N // 2 + N % 2:]
low_tide.reverse()

for i in range(N // 2):
    print(low_tide[i], high_tide[i], end=' ')
if N % 2 == 1:
    print(low_tide[-1])