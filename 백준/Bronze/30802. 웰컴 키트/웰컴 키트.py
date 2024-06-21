N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

n_t = 0
for size in sizes:
    t1, t2 = divmod(size, T)
    if t2:
        t1 += 1
    n_t += t1
p1, p2 = divmod(N, P)

print(n_t)
print(p1, p2)