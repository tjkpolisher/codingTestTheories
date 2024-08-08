D_and_V = []
for _ in range(11):
    D, V = map(int, input().split())
    D_and_V.append((D, V))

D_and_V.sort(key=lambda x: x[0])
T = [D_and_V[0][0]]
for i in range(1, 11):
    T.append(T[-1] + D_and_V[i][0])

ans = 0
for i in range(11):
    ans += (T[i] + 20 * D_and_V[i][1])
print(ans)