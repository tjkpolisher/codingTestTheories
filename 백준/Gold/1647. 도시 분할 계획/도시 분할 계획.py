import sys
input = sys.stdin.readline

N, M = map(int, input().split())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges = []
result = 0

parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
maximum_cost = 0

for edge in edges:
    C, A, B = edge
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result += C
        maximum_cost = C

print(result - maximum_cost)