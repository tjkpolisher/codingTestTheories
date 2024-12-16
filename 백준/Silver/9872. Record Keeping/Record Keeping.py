import sys
input = sys.stdin.readline

N = int(input())
groups = []
distinct_group = []
for _ in range(N):
    group = sorted(list(input().rstrip().split()))
    if group not in distinct_group:
        groups.append([group, 1])
        distinct_group.append(group)
    else:
        groups[distinct_group.index(group)][1] += 1

groups.sort(key=lambda x: x[1], reverse=True)
print(groups[0][1])