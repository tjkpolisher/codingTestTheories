N, M = map(int, input().split())
rows = 0
cols = set()

for i in range(N):
    spot = list(input())
    if "X" in spot:
        rows += 1
        for j in range(M):
            if spot[j] == "X":
                cols.add(j)
cols = len(list(cols))
print(max(N - rows, M - cols))