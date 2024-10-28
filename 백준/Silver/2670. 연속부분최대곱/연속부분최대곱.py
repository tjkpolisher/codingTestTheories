import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    array.append(float(input()))

for i in range(1, N):
    array[i] = max(array[i], array[i] * array[i - 1])

print(f"{max(array):.3f}")