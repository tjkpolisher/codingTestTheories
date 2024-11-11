A, B = map(int, input().split())
N = int(input())
frequencies = []
for _ in range(N):
    frequencies.append(int(input()))

min_press = abs(B - A)

for freq in frequencies:
    press = 1 + abs(B - freq)
    min_press = min(press, min_press)

print(min_press)