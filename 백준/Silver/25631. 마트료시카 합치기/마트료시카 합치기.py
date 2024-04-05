import sys
input = sys.stdin.readline

N = int(input().rstrip())
sizes = list(map(int, input().rstrip().split()))
sizes.sort()

cnt = 0
while sizes:
    sizes_set = set(sizes)
    for n in sizes_set:
        del sizes[sizes.index(n)]
    cnt += 1

print(cnt)