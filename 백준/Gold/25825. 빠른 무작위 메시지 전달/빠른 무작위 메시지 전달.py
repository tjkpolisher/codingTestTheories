import sys
from itertools import permutations
input = sys.stdin.readline

times = [list(map(int, input().split())) for _ in range(12)]
groups = []
for i in range(6):
    groups.append((2 * i, 2 * i + 1))

min_cost = int(1e9)
for perm in permutations(groups):
    for mask in range(1 << 6):
        cost = 0
        if mask & 1:
            cost += times[perm[0][1]][perm[0][0]]
            last = perm[0][0]
        else:
            cost += times[perm[0][0]][perm[0][1]]
            last = perm[0][1]

        valid = True
        for i in range(1, 6):
            group = perm[i]
            if mask & (1 << i):
                cost += times[last][group[1]] + times[group[1]][group[0]]
                last = group[0]
            else:
                cost += times[last][group[0]] + times[group[0]][group[1]]
                last = group[1]
        min_cost = min(min_cost, cost)

print(min_cost)