N = int(input())
cows_waiting = list(map(int, input().split()))
cows_waiting.sort(reverse=True)

in_line = 0
for i in range(N):
    if in_line <= cows_waiting[i]:
        in_line += 1

print(in_line)