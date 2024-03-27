import sys
input = sys.stdin.readline

n_A, n_B = map(int, input().rstrip().split())
A = set(map(int, input().rstrip().split()))
B = set(map(int, input().rstrip().split()))
sub1 = A - B
sub2 = B - A
ans = sub1.union(sub2)
print(len(ans))