import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())
stickers = []
for _ in range(N):
    stickers.append(list(map(int, input().split())))

stickers.sort(key=lambda x: x[0] * x[1], reverse=True)
ans = 0


def can_place(r1, c1, r2, c2):
    if r1 + r2 <= H and max(c1, c2) <= W:
        return True
    if c1 + c2 <= W and max(r1, r2) <= H:
        return True
    if r1 + r2 <= W and max(c1, c2) <= H:
        return True
    if c1 + c2 <= W and max(r1, r2) <= H:
        return True
    return False


for i in range(N):
    r1, c1 = stickers[i]
    for j in range(i + 1, N):
        r2, c2 = stickers[j]
        for (nr1, nc1) in [(r1, c1), (c1, r1)]:
            for (nr2, nc2) in [(r2, c2), (c2, r2)]:
                if can_place(nr1, nc1, nr2, nc2):
                    ans = max(ans, nr1 * nc1 + nr2 * nc2)

print(ans)