import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
dots = set()
for _ in range(N):
    dots.add(tuple(map(int, input().split())))

cnt = 0
for dot in dots:
    key1 = (dot[0] + A, dot[1]) in dots
    key2 = (dot[0], dot[1] + B) in dots
    key3 = (dot[0] + A, dot[1] + B) in dots
    if key1 and key2 and key3:
        cnt += 1

print(cnt)