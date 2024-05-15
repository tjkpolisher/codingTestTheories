N, L, W, H = map(int, input().split())
start = 0
end = max(L, W, H)

for i in range(1000):
    mid = (start + end) / 2
    if (L // mid) * (W // mid) * (H // mid) >= N:
        start = mid
    else:
        end = mid

print(f"{end:.10f}")