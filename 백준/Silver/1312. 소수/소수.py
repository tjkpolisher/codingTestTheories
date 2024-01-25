A, B, N = map(int, input().split())
for _ in range(N):
    A = (A % B) * 10
    result = A // B
print(result)