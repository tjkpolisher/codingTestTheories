import sys
input = sys.stdin.readline

N = int(input())
length = list()

for _ in range(N):
    length.append(int(input()))

length.sort(reverse=True)

ans = -1
for i in range(N - 2):
    l1 = length[i]
    l2 = length[i + 1]
    l3 = length[i + 2]
    if l1 < l2 + l3:
        ans = l1 + l2 + l3
        break

print(ans)