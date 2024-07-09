import sys
input = sys.stdin.readline

N = int(input())
coords = list(map(int, input().split()))
coords_sorted = sorted(list(set(coords)))

coords_dict = {coords_sorted[i]: i for i in range(len(coords_sorted))}
for i in coords:
    print(coords_dict[i], end=' ')