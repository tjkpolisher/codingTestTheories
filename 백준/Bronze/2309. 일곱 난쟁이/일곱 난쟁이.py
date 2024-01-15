from itertools import combinations
dwarves = []
for _ in range(9):
    dwarves.append(int(input()))
net_height = sum(dwarves)
combs = list(combinations(dwarves, 2))
for comb in combs:
    if sum(comb) == net_height - 100:
        ans = list(comb)
for i in ans:
    dwarves.remove(i)
dwarves.sort()
for d in dwarves:
    print(d)