d = list(input())
for i in range(len(d)):
    d[i] = int(d[i])
    if d[i] >= 5:
        d[i] = d[i] - 1

ans = 0
for i in range(len(d)):
    ans += d[i] * (9 ** (len(d) - i - 1))
print(ans)