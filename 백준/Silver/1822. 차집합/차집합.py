import sys
input = sys.stdin.readline

n_a, n_b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
sub = sorted(list(A - B))
print(len(sub))
if sub:
    print(*sub)