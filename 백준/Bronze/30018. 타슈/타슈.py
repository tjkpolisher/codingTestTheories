N = int(input())
initial = list(map(int, input().split()))
final = list(map(int, input().split()))

s = 0
for i in range(N):
    s += abs(initial[i] - final[i])
print(int(s / 2))